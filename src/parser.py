## This function will turn the string into the reverse polish notation

input = "3 + 4 × 2 ÷ ( 1 − 5 ) ^ 2 ^ 3"
input = input.split(' ')

nonNumbers = ['+','-','*','/','(',')','^']
operators = {'+':1,  '-':1,  '*':2,  '/':2,  '^':3}
opStack = []
output = []


for token in input:
    if token not in nonNumbers:
        output.append(token)
    elif 1==1:
        print("Hello")
