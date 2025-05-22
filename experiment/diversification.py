import json
import re
import numpy as np
import logging
import requests
import argparse
from tqdm import tqdm
from utils import *

def extract_rewritten_paragraph(text):
    start_index = text.find("Rewritten paragraph:")
    
    if start_index == -1:
        return "" 
    content_start = start_index + len("Rewritten paragraph:")
    return text[content_start:].strip()

def extract_rewrite_text(section_marker, text):
    # Split at the marker
    parts = text.split(section_marker)
    if len(parts) < 2:
        return ""
    # The section after the marker
    rewrite_section = parts[1].strip()
    return rewrite_section


def disrupt(model, type_dataset):
    if type_dataset == "FOLIO":
        path = "./data/FOLIO/dev.json"
    
    elif type_dataset == "ProverQA":
        path = "./data/ProverQA/medium.json"

    elif type_dataset == "LogicalDeduction":
        path = "./data/Deduction/dev.json"


    elif type_dataset == "ProntoQA":
        path = "./data/ProntoQA/dev.json"


    elif type_dataset == "ProofWriter":
        path = "./data/ProofWriter/dev.json"


    with open(path, 'r', encoding='utf-8') as file:
        dataset = json.load(file)

    count = 0

    dataset = dataset[:200]

    outputs = []

    for sample in tqdm(dataset):
        if type_dataset == "FOLIO":
            problem = sample["context"]
            question = sample["question"]
            with open(f'./experiment/diversification-prompts/folio.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)

        elif type_dataset == "ProverQA":
            problem = sample["context"]
            question = sample["question"]
            with open(f'./experiment/diversification-prompts/folio.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)


        elif type_dataset == "LogicalDeduction":
            problem = sample["context"]
            question = sample["question"]
            options = sample["options"]
            options = "\n".join(options)
            with open(f'./experiment/diversification-prompts/ld.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem)

        elif type_dataset == "ProntoQA":
            problem = sample["context"]
            question = sample["question"]
            with open(f'./experiment/diversification-prompts/pronto.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)


        elif type_dataset == "ProofWriter":
            problem = sample["context"]
            question = sample["question"]
            with open(f'./experiment/diversification-prompts/pw.txt', 'r', encoding='utf-8') as f:
                prompt_template = f.read()
            full_prompt = prompt_template.replace('[[PROBLEM]]', problem).replace('[[QUESTION]]', question)
        
        output = LLM_response(full_prompt, model)
        disrupted_context = output

        # create output
        output = {
            'id': sample['id'],
            'context': sample['context'],
            'question': sample['question'],
            'answer': sample['answer'],
            'disrupted_context': disrupted_context,
        }

        if 'options' in sample:
            output['options'] = sample['options']

        outputs.append(output)
    
    def serialize(obj):
        if isinstance(obj, Exception):
            return repr(obj) 
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    with open(f'./outputs/disrupt/{type_dataset}_{model}.json', 'w', encoding="utf-8") as f:
        json.dump(outputs, f, indent=2, ensure_ascii=False, default=serialize)
        
def disrupt_result(type_dataset, model):
    with open(f'./outputs/disrupt/{type_dataset}_{model}.json', encoding="utf-8") as f:
        dataset = json.load(f)

    err_count = 0
    outputs = []
    for example in tqdm(dataset):
        text = example['disrupted_context']
        context_text = extract_rewritten_paragraph(text)
        
        if context_text == "":
            context_text = example['context']
            err_count += 1
            
        
        output = {
            'id': example['id'],
            'context': context_text,
            'question': example['question'],
            'answer': example['answer'],
        }

        if 'options' in example:
            output['options'] = example['options']

        outputs.append(output)

    with open(f'./data/{type_dataset}/disrupt.json', 'w', encoding="utf-8") as f:
        json.dump(outputs, f, indent=2, ensure_ascii=False)
    print(f"Error count: {err_count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', type=str)
    parser.add_argument('--backup_strategy', type=str, default='random', choices=['random'])
    parser.add_argument('--backup_LLM_result_path', type=str, default='../baselines/results')
    parser.add_argument('--model_name', type=str, default='gpt-4-1106-preview')
    parser.add_argument('--timeout', type=int, default=60)

    args = parser.parse_args()

    disrupt(args.model_name, args.dataset_name)
    disrupt_result(args.dataset_name, args.model_name)