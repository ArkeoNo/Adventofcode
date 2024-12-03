import re

def extract_and_mul(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Définition des patterns
    mul_pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    # Split des tokens
    tokens = re.split(r'(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do\(\)|don\'t\(\))', data)

    enabled = True
    total = 0

    for token in tokens:
        if do_pattern.match(token):
            enabled = True
        elif dont_pattern.match(token):
            enabled = False
        elif enabled and mul_pattern.match(token):
            a, b = mul_pattern.findall(token)[0]
            total += int(a) * int(b)

    return total

print(extract_and_mul('input/3-3.txt'))