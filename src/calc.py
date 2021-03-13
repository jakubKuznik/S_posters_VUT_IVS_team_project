###########################################
# Project name: IVS - projekt
# File: calc.py
# Date: 13. 03. 2021
# Last change: 13. 03. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: Calculator
###########################################

## @file calc.py
#
#  @brief calculator

import time
# Mathematical library of all operation and Exceptions
import math_lib


## Documentation for a function.
#  This is how doxygen function documentation looks like .
def main():

    ## THIS COMMENT WILL BE IN DOXYGEN
    print(math_lib.fact(-5))
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
