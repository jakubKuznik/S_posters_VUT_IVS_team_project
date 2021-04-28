# ##########################################
# Project name: IVS - projekt
# File: standard_deviation.py
# Date: 24. 04. 2021
# Last change: 28. 04. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
# ##########################################

## A ternary script used for profiling. Calculates the standard deviation of a set of inputs.
#
#  @package standard_deviation
#  @file standard_deviation.py
#  @brief A ternary script used for profiling. Calculates the standard deviation of a set of inputs.
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import math_lib   ## our math library
import sys
import select

##
# @brief Function separates the input into an array of floats.  
# 
# @param input_str string in that the stdin is stored
# @return arr array of floats
def separate_numbers(input_str):
    # input string contains characters that are replaced with whitespace and than splitted in an array
    input_str = str(input_str).replace("[", ' ').replace("]", ' ').replace("\\n", ' ').replace("\\t", ' ').replace("\'", ' ').replace(",", ' ').split()
    
    # converts every integer value to float and insert in arr
    arr = []

    for item in input_str:
        try:
            arr.append(float(item))
        except:
            print("Error: \"" + item + "\" not a number")
            exit(1)

    return arr

##
# @brief Function calculates the mean.
# 
# @param input_array of floats that are used to calculate the mean
# @return mean
#
def mean(input_array):
    arr_size = len(input_array)     # number of elements in input_array
    total_sum = 0.0                 # sum of numbers in array
    
    for i in range(arr_size):
        total_sum = math_lib.add(total_sum, input_array[i])
    
    return math_lib.div(total_sum, arr_size)

##
# @brief Function calculates the standard deviation.
# 
# @param input_array of floats that are used to calculate the standard deviation
# @return standard deviation
#
def std_dev(input_array):
  arr_size = len(input_array)     # number of elements in input_array
  avg = mean(input_array)        # count the mean
  total_sum = 0.0                 # sum of numbers in array
  
  for i in range(arr_size):
    tmp_res = math_lib.sub(input_array[i], avg)
    tmp_res = math_lib.exp(tmp_res, 2)
    total_sum = math_lib.add(total_sum, tmp_res)
  
  tmp_res = math_lib.div(total_sum, arr_size)
  return math_lib.root(tmp_res, 2)


def main():
    # read input
    print("Enter numbers: \n")
    input_str = ""
    input_str = sys.stdin.readlines()

    # separate input into an array of floats
    arr = separate_numbers(input_str)

    # count the standard deviation
    print(std_dev(arr))


if __name__ == '__main__':
    main()

## end of file profiling.py