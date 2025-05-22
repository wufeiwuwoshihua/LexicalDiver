import json
import os
from tqdm import tqdm
from symbolic_solvers.fol_solver.prover9_solver import FOL_Prover9_Program
from symbolic_solvers.pyke_solver.pyke_solver import Pyke_Program
from symbolic_solvers.csp_solver.csp_solver import CSP_Program
from symbolic_solvers.z3_solver.sat_problem_solver import LSAT_Z3_Program
import argparse
import random
from backup_answer_generation import Backup_Answer_Generator
import shutil
import re

def extract_logic_program_block(text, type):
    if type == "FOLIO" or "ProofWriter" or "ProverQA":
        pattern = re.compile(r"(Predicates:.*?Question:.*?$)", re.DOTALL)
        matches = list(pattern.finditer(text))
        if matches:
            return matches[-1].group(1)
        else:
            return "unfind"
    elif type == "ProntoQA":
        pattern = re.compile(r"(Predicates:.*?Query:.*?$)", re.DOTALL)
        match = pattern.search(text)
        if match:
            return match.group(1)
        else:
            return "unfind"
    
    elif type == "LogicalDeduction":
        pattern = re.compile(r"(Domain:.*?Query:.*?$)", re.DOTALL)
        match = pattern.search(text)
        if match:
            return match.group(1)
        else:
            return "unfind"


class LogicInferenceEngine:
    def __init__(self, args):
        self.args = args
        self.dataset_name = args.dataset_name
        self.model_name = args.model_name
        self.backup_strategy = args.backup_strategy

        self.dataset = self.load_logic_programs()
        program_executor_map = {'ProntoQA': Pyke_Program, 
                                'ProverQA': FOL_Prover9_Program,
                                'ProofWriter2': Pyke_Program,
                                'ProofWriter': FOL_Prover9_Program,
                                'FOLIO': FOL_Prover9_Program,
                                'LogicalDeduction': CSP_Program,
                                'AR-LSAT': LSAT_Z3_Program}
        self.program_executor = program_executor_map[self.dataset_name]
        self.backup_generator = Backup_Answer_Generator(self.dataset_name, self.backup_strategy, self.args.backup_LLM_result_path)

    def load_logic_programs(self):
        with open(os.path.join('./outputs/trans', f'{self.dataset_name}_{self.model_name}.json'), encoding="utf-8") as f:
            dataset = json.load(f)
        return dataset
    
    def save_results(self, outputs):

        def serialize(obj):
            if isinstance(obj, Exception):
                return repr(obj)
            raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

        with open(f'./outputs/inference/{self.dataset_name}_{self.model_name}.json', 'w', encoding="utf-8") as f:
            json.dump(outputs, f, indent=2, ensure_ascii=False, default = serialize)

    def safe_execute_program(self, id, logic_program):
        if self.dataset_name == 'ProofWriter2':
            dataset_name = 'ProofWriter'
        else:
            dataset_name = self.dataset_name
        program = self.program_executor(logic_program, dataset_name)
        # cannot parse the program
        if program.flag == False:
            answer = self.backup_generator.get_backup_answer(id)
            return answer, 'parsing error', ''
        # execuate the program
        answer, error_message = program.execute_program()
        # not executable
        if answer is None:
            answer = self.backup_generator.get_backup_answer(id)
            return answer, 'execution error', error_message
        # successfully executed
        answer = program.answer_mapping(answer)
        return answer, 'success', ''

    def inference_on_dataset(self):
        outputs = []
        error_count = 0
        
        for example in tqdm(self.dataset):
            answer, flag, error_message = self.safe_execute_program(example['id'], example['raw_logic_programs'][0].strip())
            if not flag == 'success':
                error_count += 1

            # create output
            output = {'id': example['id'], 
                    'context': example['context'],
                    'question': example['question'], 
                    'answer': example['answer'],
                    'raw_logic_programs': example['raw_logic_programs'],
                    'LLM_output': example['LLM_output'],
                    'flag': flag,
                    'error_message': error_message,
                    'predicted_answer': answer}
            
            if 'options' in example:
                output['options'] = example['options']

            outputs.append(output)
        
        print(f"Error count: {error_count}")
        self.save_results(outputs)
        self.cleanup()

    def cleanup(self):
        complied_krb_dir = './pre_experiment/compiled_krb'
        if os.path.exists(complied_krb_dir):
            print('removing compiled_krb')
            shutil.rmtree(complied_krb_dir)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', type=str)
    parser.add_argument('--backup_strategy', type=str, default='random', choices=['random'])
    parser.add_argument('--backup_LLM_result_path', type=str, default='../baselines/results')
    parser.add_argument('--model_name', type=str, default='gpt-4-1106-preview')
    parser.add_argument('--timeout', type=int, default=60)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    engine = LogicInferenceEngine(args)
    engine.inference_on_dataset()