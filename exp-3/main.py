import itertools

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars = '!@#$%^&*'

all_chars = lower + upper + chars


def generate_file(length, filename):
    with open(filename, 'w') as f:
        for combo in itertools.product(all_chars, repeat = length):
            f.write(''.join(combo) + '\n')

def crack_pass(target, filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
            word = line.strip()
            if word == target:
                print(f'match found {word} at attempt of {count}')
                return
length = int(input('Enter the length of the pass : '))
target = input(f'Enter the password with in the given length of {length} : ')

filename = 'dict.txt'

generate_file(length, filename)
crack_pass(target, filename)