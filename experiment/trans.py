import json
import re
import numpy as np
import logging
import requests
import argparse
from tqdm import tqdm
from utils import *

import os

import logging

def extract_logic_program_block(text, type):
    if type == "FOLIO" or "ProofWriter" or "ProverQA":
        pattern = re.compile(r"(Premises:.*?Question:.*?$)", re.DOTALL)
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

def translation(model, type_dataset, disrupt, noes, synonym, tuning):
    logger = logging.getLogger('my_app')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('folio.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    if disrupt == 'True':

        if type_dataset == "FOLIO":
            path = "./data/FOLIO/disrupt.json"

        elif type_dataset == "ProverQA":
            path = "./data/ProverQA/disrupt.json"

        elif type_dataset == "LogicalDeduction":
            path = "./data/Deduction/disrupt.json"


        elif type_dataset == "ProntoQA":
            path = "./data/ProntoQA/disrupt.json"


        elif type_dataset in ("ProofWriter", "ProofWriter2"):
            path = "./data/ProofWriter/disrupt.json"
            
            
    else:
        if type_dataset == "FOLIO":
            path = "./data/FOLIO/dev.json"

        elif type_dataset == "ProverQA":
            path = "./data/ProverQA/medium.json"


        elif type_dataset == "LogicalDeduction":
            path = "./data/Deduction/dev.json"


        elif type_dataset == "ProntoQA":
            path = "./data/ProntoQA/dev.json"


        elif type_dataset in ("ProofWriter", "ProofWriter2"):
            path = "./data/ProofWriter/dev.json"


    with open(path, 'r', encoding='utf-8') as file:
        dataset = json.load(file)
    

    dataset = dataset[:200]
    outputs = []

    for sample in tqdm(dataset):
        if type_dataset == "FOLIO":
            problem = sample["context"]
            question = sample["question"]
            if synonym == 'True':
                with open(f'./experiment/synonym-prompts/FOLIO.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/FOLIO-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./experiment/direct-prompts/FOLIO.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
            # print(full_prompt)
            # break
        
        elif type_dataset == "ProverQA":
            problem = sample["context"]
            question = sample["question"]
            if synonym == 'True':
                with open(f'./experiment/synonym-prompts/FOLIO.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/FOLIO-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./experiment/direct-prompts/FOLIO.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)


        elif type_dataset == "LogicalDeduction":
            problem = sample["context"]
            question = sample["question"]
            options = sample["options"]
            options = "\n".join(options)
            if synonym == 'True':
                with open(f'./experiment/synonym-prompts/LD-1.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/LogicalDeduction-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./experiment/direct-prompts/LogicalDeduction.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question).replace('[[CHOICES]]', options)


        elif type_dataset == "ProntoQA":
            problem = sample["context"]
            question = sample["question"]
            if synonym == 'True':  
                with open(f'./experiment/synonym-prompts/ProntoQA.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/ProntoQA-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./experiment/direct-prompts/ProntoQA.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)


        elif type_dataset == "ProofWriter":
            problem = sample["context"]
            question = sample["question"]
            if synonym == 'True':
                with open(f'./experiment/synonym-prompts/pw.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/FOLIO-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./experiment/direct-prompts/FOLIO.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        
        elif type_dataset == "ProofWriter2":
            problem = sample["context"]
            question = sample["question"]
            if synonym == 'True':
                with open(f'./experiment/synonym-prompts/pw2.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            elif tuning == 'True':
                with open(f'./experiment/direct-prompts/ProofWriter-tuning.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            else:
                with open(f'./pexperiment/direct-prompts/ProofWriter.txt', 'r', encoding='utf-8') as f:
                    prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        
        
        
        LLM_output = LLM_response(full_prompt, model)
        programs = LLM_output
        if synonym == 'True':
            programs = extract_logic_program_block(programs, type_dataset)

        programs = [programs]


        output = {
            'id': sample['id'],
            # 'trial': i,
            'context': sample['context'],
            'question': sample['question'],
            'answer': sample['answer'],
            'LLM_output': LLM_output,
            'raw_logic_programs': programs,
        }

        if 'options' in sample:
            output['options'] = sample['options']

        outputs.append(output)

    
    def serialize(obj):
        if isinstance(obj, Exception):
            return repr(obj) 
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    if noes == 'True':
        with open(f'./outputs/trans/{type_dataset}_{model}_noes.json', 'w', encoding="utf-8") as f:
            json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
    elif synonym == 'True':
        if disrupt == 'True':
            with open(f'./outputs/trans/{type_dataset}_{model}_synonym_disrupt.json', 'w', encoding="utf-8") as f:
                json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
        else:
            with open(f'./outputs/trans/{type_dataset}_{model}_synonym.json', 'w', encoding="utf-8") as f:
                json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
    elif disrupt == 'True':
        if tuning == 'True':
            with open(f'./outputs/trans/{type_dataset}_{model}_disrupt_tuning.json', 'w', encoding="utf-8") as f:
                json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
        else:
            with open(f'./outputs/trans/{type_dataset}_{model}_disrupt.json', 'w', encoding="utf-8") as f:
                json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
    else:
        with open(f'./outputs/trans/{type_dataset}_{model}.json', 'w', encoding="utf-8") as f:
            json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', type=str)
    parser.add_argument('--backup_strategy', type=str, default='random', choices=['random'])
    parser.add_argument('--model_name', type=str, default='gpt-4-1106-preview')
    parser.add_argument('--timeout', type=int, default=60)
    parser.add_argument('--disrupt', type=str, default='False', choices=['True', 'False'])
    parser.add_argument('--noes', type=str, default='False', choices=['True', 'False'])
    parser.add_argument('--synonym', type=str, default='False', choices=['True', 'False'])
    parser.add_argument('--tuning', type=str, default='False', choices=['True', 'False'])

    args = parser.parse_args()

    translation(args.model_name, args.dataset_name, args.disrupt, args.noes, args.synonym, args.tuning)