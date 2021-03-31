## This function will turn the string into the reverse polished notation

input_str = "3 + 4 × 2 ÷ ( 1 − 5 ) ^ 2 ^ 3"
input_str = input_str.split(' ')

nonNumbers = ['+', '-', '*', '/', '(', ')', '^']
operators = {'+': 1,  '-': 1, '*': 2, '/': 2, '^': 3}
opStack = []
output = []


for token in input_str:
    if token not in nonNumbers:
        output.append(token)
    else:
        print("Hello")
