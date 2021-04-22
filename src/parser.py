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

from math_lib import *
import re

input_str = "15 + 22.6 * 3-4 / 2"
input_str = input_str.split(' ')

nonNumbers = ['+', '-', '*', '/', '(', ')', '^']
operators = {'(':0,')':0,'+': 1, '-': 1, '*': 2, '/': 2, '&': 3, '$':3, '!':4}
opStack = []
output = []

def SplitString(CalcString):

    parentheses_counter = 0
    for i in CalcString:
        if i == "(":
            parentheses_counter += 1
        elif i == ")":
            parentheses_counter -= 1
        if parentheses_counter < 0:
            return False

    split_string = re.findall(r'[0-9\.]+|[^0-9\.]', CalcString)
    print(split_string)
    for i in range(len(split_string)-1):
        if split_string[0]=='-' and isNumber(split_string[1]):
            split_string[1]='-'+split_string[1]
            del split_string[0]
        elif split_string[i]=='-' and split_string[i-1] == '(' and isNumber(split_string[i+1]):
            split_string[i+1]='-'+split_string[i+1]
            del split_string[i]
    SolveFactorials(split_string)
    infixToRPN(split_string)

def SolveFactorials(split_string):
    print(split_string)
    for i in range(len(split_string)-1):
        if split_string[i]=='!':
            FactValue = fact(int(split_string[i-1]))
            split_string[i-1]=FactValue
            del split_string[i]

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
                if operators[operator]>=operators[i]:
                    RPN_array.append(stack.pop())
            stack.append(i)

    while len(stack)!=0:
        RPN_array.append(stack.pop())
    print(RPN_array)
    RPNEval(RPN_array)


def RPNEval(RPN_array):
    stack=[]
    temp=[0,0]
    value=0
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
    result=stack[0]
    print(result)
    return result

def isNumber(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

SplitString('4!+5')