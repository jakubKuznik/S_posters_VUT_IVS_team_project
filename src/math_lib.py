#TODO HLAVICKA

class DivByZero(Exception):
    pass


class DomainError(Exception):
    pass


## This function will return sum of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def add(a, b):
    return a+b


## This function will return difference of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def sub(a, b):
    return a-b


## This function will return multiple of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def mult(a, b):
    return a*b


## This function will return multiple of two numbers.
#  This is how doxygen function documentation looks like.
#  @param a first operand
#  @param b second operand
def div(a, b):
    if b == 0:
        print("lmao")
        raise DivByZero

    return a/b
