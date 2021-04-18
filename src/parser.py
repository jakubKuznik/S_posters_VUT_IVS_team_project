###########################################
# Project name: IVS - projekt
# File: parser.py
# Date: 14. 03. 2021
# Last change: 15. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Parser
###########################################

## @file parser.py
#
#  @brief parser
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

## This function will turn the string into the reverse polish notation
input_str = "3 + 4 × 2 ÷ ( 1 − 5 ) ^ 2 ^ 3"
input_str = input_str.split(' ')

nonNumbers = ['+', '-', '*', '/', '(', ')', '^']
operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
opStack = []
output = []


for token in input_str:
    if token not in nonNumbers:
        output.append(token)
    elif 1 == 1:
        print("Hello")
