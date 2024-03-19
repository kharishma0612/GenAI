import random

def build_chain(filename, chain_length):
    with open(filename, 'r') as file:
        text = file.read().split()
    chain = {}
    for i in range(len(text) - chain_length):
        prefix = tuple(text[i:i + chain_length])
        suffix = text[i + chain_length]
        if prefix in chain:
            chain[prefix].append(suffix)
        else:
            chain[prefix] = [suffix]

    return chain

def generate(filename, start_words, chain_length, num_generated):
    chain = build_chain(filename, chain_length)
    if len(start_words) != chain_length:
        raise ValueError("Length of start_words list must be exactly equal to chain_length")
    prefix = tuple(start_words)
    generated_words = list(start_words)
    for _ in range(num_generated):
        if prefix in chain:
            next_word = random.choice(chain[prefix])
            generated_words.append(next_word)
            prefix = tuple(generated_words[-chain_length:])
        else:
            break

    return ' '.join(generated_words)
filename = 'myfile.txt'
start_words = ['Shall', 'I', 'compare', 'thee', 'to', 'a', 'summer’s', 'day?',
               'Thou', 'art', 'more', 'lovely', 'and', 'more', 'temperate:',
               'Rough', 'winds', 'do', 'shake', 'the', 'darling', 'buds', 'of', 'May,']

chain_length = 24
num_generated = 200
try:
    generated_text = generate(filename, start_words, chain_length, num_generated)
    print(generated_text)
except ValueError as e:
    print("Error:", e)
