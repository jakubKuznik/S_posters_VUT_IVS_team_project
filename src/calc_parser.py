###########################################
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
# Brief: Parser
###########################################

## @file calc_parser.py
#
#  @brief parser
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

## This function will turn the string into the reverse polish notation

from math_lib import *
import re


nonNumbers = ['+', '-', '*', '/', '(', ')', '^']
operators = {'(':0,')':0,'+': 1, '-': 1, '*': 2, '/': 2, '?':2, '&': 3, '$':3, '!':3}
opStack = []
output = []

def SplitString(CalcString):
    split_string = re.findall(r'[0-9\.]+|[^0-9\.]', CalcString)

    if not validate(split_string):
        return "Syntax Error"

    for i in range(len(split_string)-1):
        if i == 0 and split_string[i]=='-' and isNumber(split_string[1]):
            split_string[0]='@'
        elif split_string[i]=='-' and split_string[i-1] == '(' and isNumber(split_string[i+1]):
            split_string[i]='@'
    minus_list=[]
    for i in range(len(split_string)):
        if split_string[i]!='@':
            minus_list.append(split_string[i])
        else:
            minus_list.append('-1')
            minus_list.append('*')

    return infixToRPN(minus_list)

def infixToRPN(Infix_array):
    RPN_array=[]
    stack=[]
    for i in Infix_array:
        if isNumber(i):
            RPN_array.append(i)
        elif i =='(':
            stack.append(i)
        elif i == ')':
            top = stack.pop()
            while top!= '(':
                RPN_array.append(top)
                top=stack.pop()
        else:
            for operator in stack[::-1]:
                if operator == '(':
                    break
                if operators[operator]>=operators[i] and operator!='&':
                    RPN_array.append(stack.pop())
            stack.append(i)

    while len(stack)!=0:
        RPN_array.append(stack.pop())
    return RPNEval(RPN_array)


def RPNEval(RPN_array):
    stack=[]
    temp=[0,0]
    for i in RPN_array:
        if isNumber(i):
            stack.append(i)
        else:
            temp[1]=stack.pop()
            temp[0]=stack.pop()
            if i =='$':
                value = root(float(temp[0]),float(temp[1]))
                stack.append(value)
            if i=='&':
                value = exponentiation(float(temp[0]),float(temp[1]))
                stack.append(value)
            elif i=='*':
                value = mult(float(temp[0]),float(temp[1]))
                stack.append(value)
            elif i=='+':
                value = add(float(temp[0]),float(temp[1]))
                stack.append(value)
            elif i=='-':
                value = sub(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i=='/':
                value = div(float(temp[0]), float(temp[1]))
                stack.append(value)
            elif i == '!':
                value =fact(float(temp[0]))
                stack.append(value)
            elif i == '?':
                value = modulo(float(temp[0]), float(temp[1]))
                stack.append(value)
    result=stack[0]
    return result

def isNumber(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

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

    binary_operators = ['+', '-','*','/','&','$','?']
    for i in range(len(split_string)):
        if split_string[i]==')':
            if split_string[i-1]=='(' or split_string[i-1] in binary_operators:
                return False
        elif split_string[i]=='(':
            if i!=0:
                if split_string[i-1] == ')':
                    return False
                elif split_string[i-1] not in binary_operators:
                    return False
        elif split_string[i]== '+':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '-':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '*':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '/':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '&':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '$':
            if i==0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        elif split_string[i] == '!':
            if i==0:
                return False
        elif split_string[i] == '?':
            if i == 0:
                return False
            if split_string[i-1] in binary_operators:
                return False
        else:
            if split_string[i][0]=='.':
                return False
            if split_string[i].count(".")>1:
                return False
            if split_string[i][0]=='0' and len(split_string[i])!=1 and split_string[i].count(".")==0:
                return False
            if split_string[i].count(".")==1:
                decimal_location = split_string[i].index('.')
                tested_list = split_string[i][:decimal_location]
                if tested_list[0]=='0' and len(tested_list)!=1:
                    return False
    return True