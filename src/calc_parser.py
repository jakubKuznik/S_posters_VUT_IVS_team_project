# ##########################################
# Project name: IVS - projekt
# File: calc_parser.py
# Date: 14. 03. 2021
# Last change: 15. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Calculator Parser
# ##########################################

## Calculator Parser
#
#  @package calc_parser
#  @file calc_parser.py
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import re
from math_lib import *

##
nonNumbers = ['+', '-', '*', '/', '?', '&', '$']
##
operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '?': 2, '&': 3, '$': 3, '!': 3}
##
opStack = []
##
output = []


##
# @brief
#
# @param
#
def split_string_fn(calc_string, displayed_content):
    for i in range(1, len(displayed_content)-1):
        if displayed_content[i] == 'π' or displayed_content[i] == 'M':
            if is_number(displayed_content[i - 1]) or is_number(displayed_content[i + 1]):
                return "Syntax Error"
    for i in range(1, len(displayed_content)):
        if displayed_content[i] == 'π' or displayed_content[i] == 'M':
            if displayed_content[i - 1] == 'M':
                return "Syntax Error"
            if displayed_content[i - 1] == 'π':
                return "Syntax Error"
            if displayed_content[i - 1] == ')':
                return "Syntax Error"

    calc_string = ''.join(calc_string)
    split_string = re.findall(r'[0-9.]+|[^0-9.]', calc_string)

    if calc_string[-1] in nonNumbers:
        return "Syntax Error"

    if not validate(split_string):
        return "Syntax Error"

    for i in range(len(split_string) - 1):
        if i == 0 and split_string[i] == '-' and (is_number(split_string[1]) or split_string[1]=='('):
            split_string[0] = '@'
        elif split_string[i] == '-' and split_string[i - 1] == '(' and is_number(split_string[i + 1]):
            split_string[i] = '@'
    minus_list = []
    for i in range(len(split_string)):
        if split_string[i] != '@':
            minus_list.append(split_string[i])
        else:
            minus_list.append('-1')
            minus_list.append('*')
    print(minus_list)
    return infix_to_rpn(minus_list)


## This function will turn the string into the reverse polish notation?
# @brief
#
# @param
#
def infix_to_rpn(infix_array):
    rpn_array = []
    stack = []
    for i in infix_array:
        if is_number(i):
            rpn_array.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            top = stack.pop()
            while top != '(':
                rpn_array.append(top)
                top = stack.pop()
        else:
            for operator in stack[::-1]:
                if operator == '(':
                    break
                if i!='&':
                    if operators[operator] >= operators[i]:
                        rpn_array.append(stack.pop())
                else:
                    if operators[operator] >= operators[i] and operator!='&':
                        rpn_array.append(stack.pop())
            stack.append(i)

    while len(stack) != 0:
        rpn_array.append(stack.pop())
    print(rpn_array)
    return rpn_eval(rpn_array)


##
# @brief
#
# @param
#
def rpn_eval(rpn_array):
    stack = []
    temp = [0, 0]
    for i in rpn_array:
        if is_number(i):
            stack.append(i)
        else:
            temp[1] = stack.pop()
            temp[0] = stack.pop()
            if i == '$':
                value = root(float(temp[0]), float(temp[1]))
                stack.append(value)
            if i == '&':
                value = exp(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '*':
                value = mult(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '+':
                value = add(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '-':
                value = sub(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '/':
                value = div(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '!':
                value = fact(float(temp[0]))
                stack.append(value)
            elif i == '?':
                value = mod(float(temp[0]), float(temp[1]))
                stack.append(value)
    result = stack[0]
    return result


##
# @brief
#
# @param
#
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


##
# @brief
#
# @param
#
def validate(split_string):
    # TODO: cislo nemoze koncit bodkou a nemozu byt dve cisla za sebou
    parentheses_counter = 0
    for i in split_string:
        if i == "(":
            parentheses_counter += 1
        elif i == ")":
            parentheses_counter -= 1
        if parentheses_counter < 0:
            return False
    if parentheses_counter!=0:
        return False

    binary_operators = ['+', '-', '*', '/', '&', '$', '?']
    for i in range(len(split_string)):
        if split_string[i] == ')':
            if split_string[i - 1] == '(' or split_string[i - 1] in binary_operators:
                return False
            if i!=len(split_string)-1:
                if is_number(split_string[i + 1]):
                    return False
        elif split_string[i] == '(':
            if i != 0:
                if split_string[i - 1] == ')':
                    return False
                elif split_string[i - 1] not in binary_operators and split_string[i - 1] != '(':
                    return False
                if is_number(split_string[i - 1]):
                    return False
        elif split_string[i] == '+':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '-':
            if split_string[i - 1] in binary_operators and split_string[i - 1] != '(':
                return False
        elif split_string[i] == '*':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '/':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '&':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '$':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '!':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        elif split_string[i] == '?':
            if i == 0:
                return False
            if split_string[i - 1] in binary_operators or split_string[i - 1] == '(':
                return False
        else:
            if split_string[i][0] == '.':
                return False
            if split_string[i][-1]=='.':
                return False
            if split_string[i].count(".") > 1:
                return False
            if split_string[i][0] == '0' and len(split_string[i]) != 1 and split_string[i].count(".") == 0:
                return False
            if split_string[i].count(".") == 1:
                decimal_location = split_string[i].index('.')
                tested_list = split_string[i][:decimal_location]
                if tested_list[0] == '0' and len(tested_list) != 1:
                    return False
    return True
