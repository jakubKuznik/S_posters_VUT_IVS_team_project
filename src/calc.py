#TODO HLAVICKA




import time
import math_lib #Math library containing all the math operation.


## Documentation for a function.
#  This is how doxygen function documentation looks like .
def main():

    ## THIS COMMENT WILL BE IN DOXYGEN
    print(math_lib.add(9, 5))
    # THIS COMENT WILL NOT BE IN DOXYGEN

    #while true(do MATH)
        #read numbers | operation
        #do operation
        #print result


    return 0






#This is hou the main function is defined in python
if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
