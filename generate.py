import random
import json
import argparse

def generate(args):
    model = open(args.model, 'r', encoding='utf-16')
    corpusstr = model.read()
    corpus = json.loads(corpusstr)

    print(args.seed, end=' ')
    keys = corpus[args.seed].keys()
    keys = list(keys)
    choosen = random.choice(keys)

    for i in range(args.length - 1):
        print(choosen, end=' ')
        next_keys = corpus[choosen].keys()
        next_k = list(next_keys)
        choosen = random.choice(next_k)
        if next_k != ['END']:
            while choosen == 'END':
                choosen = random.choice(next_k)  
        else:
            break

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', '--model')
    parser.add_argument('-length', '--length')
    parser.add_argument('-seed', '--seed')
    parser.add_argument('-output', '--output')
    return parser.parse_args()

def main():
    args_namespace = parse_args()
    generate(args_namespace)

main()
