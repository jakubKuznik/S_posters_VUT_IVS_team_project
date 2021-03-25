###########################################
# Project name: IVS - projekt
# File: math_lib.py
# Date: 13. 03. 2021
# Last change: 13. 03. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Math library
###########################################

## @file math_lib.py
#
#  @brief math library
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

class DivByZero(Exception):
    pass

class DomainError(Exception):
    pass


## This function will return the result of addition of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def add(a, b):
    return a+b


## This function will return the result of substraction of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def sub(a, b):
    return a-b


## This function will return the result of multiplication of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def mult(a, b):
    return a*b


## This function will return the result of division between two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def div(a, b):
    if b == 0:
        raise DivByZero

    return a/b


## This function will return the b-th root of a.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def root(a, b):
    if b < 0:
        raise DomainError
    return a**(1/b)


## This function will return the factorial of a given positive integer..
#  This is how doxygen function documentation looks like.
#  @param factorized_number 
def fact(factorized_number):
    if type(factorized_number)!=int or factorized_number<0:
        raise DomainError
    if factorized_number == 0:
        return 1
    else:
        return factorized_number*fact(factorized_number-1)

def exponentiation(base, power):
    if type(power) !=int or power<0 or (power == 0 and base == 0):
        raise DomainError
    return base ** power

