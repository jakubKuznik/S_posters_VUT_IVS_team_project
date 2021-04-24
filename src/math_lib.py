###########################################
# Project name: IVS - projekt
# File: math_lib.py
# Date: 13. 03. 2021
# Last change: 20. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Math library
###########################################

##
# @package math_lib
# @file math_lib.py
#
# @brief math library
#
# @author Vaňo Michal
# @author Kuzník Jakub
# @author Kratochvíl Pavel
# @author Svobodová Lucie

## Division by zero exception
# @brief Raised when the user input implies division by zero.
#
#
class DivByZeroException(Exception):
    pass

## Domain error exception
# @brief Raised when the supplied operand is out of domain of given function(e.g. sqrt(<negative number>)).
#
#
class DomainErrorException(Exception):
    pass


## 
# @brief Function returns the result of addition of two numbers.
#
# @param a first addend
# @param b second addend
# @return sum of two numbers
def add(a, b):
    return a+b


## 
# @brief This function will return the result of subtraction of two numbers.
#
# @param a first operand
# @param b second operand
# @return difference of two numbers
def sub(a, b):
    return a-b


## 
# @brief This function will return the result of multiplication of two numbers.
# 
# @param a first factor
# @param b second factor
# @return product of two numbers
def mult(a, b):
    return a*b


## 
# @brief This function will return the result of division between two numbers.
# 
# @param a dividend
# @param b divisor
# @exception DivByZero in case the divisor is equal to zero
# @return quotient of two numbers
def div(a, b):
    if b == 0:
        return "Math Error"
    return a/b


## 
# @brief Function will return the b-th root of a.
#
# @param a the base
# @param b the degree
# @exception DomainError when b is negative value
# @return b-th root of a
def root(a, b):
    if a == 0 and b == 0:
        return "Math Error"
    if a < 0:
        if b%2==1:
            return -1*a**(1/b)
        else:
            return "Math Error"
    return a**(1/b)


## 
# @brief This function will return the factorial of a given positive integer.
#
# @param factorizedNumber factorial of this number will be calculated
# @exception DomainError in case factorizedNumber is not integer or is negative
# @return factorial of number factorizedNumber
def fact(factorized_number):
    if factorized_number < 0 or not factorized_number.is_integer():
        return "Math Error"
    if factorized_number == 0:
        return 1
    else:
        return factorized_number * fact(factorized_number - 1)


## 
# @brief This function will return the result of exponentiation.
#
# @param base base of the power
# @param exponent power value
# @exception DomainError when exponent and base are both equal to zero
# @return base raised to the power of exponent
def exp(base, exponent):
    if exponent == 0 and base == 0:
        return "Math Error"
    return base ** exponent


## 
# @brief This function will return the remainder of division between two numbers.
#
# @param a dividend
# @param b divisor
# @exception DivByZero when the divisor is equal to zero
# @return remainder of a divided by b
def modulo(a, b):
    if b == 0:
        return "Math Error"
    return a % b
