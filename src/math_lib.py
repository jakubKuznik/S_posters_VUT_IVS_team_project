#TODO HLAVICKA

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


## This function will return the factorial of a given positive integer..
#  This is how doxygen function documentation looks like.
#  @param factorized_number 
def fact(factorized_number):
    if type(factorized_number)==int and factorized_number<0:
        raise DomainError
    if factorized_number == 0:
        return 1
    else:
        return factorized_number*fact(factorized_number-1)

