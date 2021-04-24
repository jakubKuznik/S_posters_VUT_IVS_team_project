###########################################
# Project name: IVS - projekt
# File: test_calc_tdd.py
# Date: 13. 03. 2021
# Last change: 13. 03. 2021
# Team: S_POSTERS
# Supervisor: ...
# Authors:  Vaňo Michal
#           Kuzník Jakub
#           Kratochvíl Pavel
#           Svobodová Lucie
#
# Brief: tests
###########################################

## @file test_calc_tdd.py
#
#  @brief tests
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import unittest
import math_lib

## Documentation for a class.
#
#  Unit Test for basic mathematical operation e.g. addition
#  subtraction, multiplication, division.
class TestBasicOperations(unittest.TestCase):
    ## Set of tests for addition
    #  @param self The object pointer.
    def test_add(self):
        result_pos_operands = math_lib.add(7, 7)
        self.assertEqual(result_pos_operands, 14)

        result_neg_operands = math_lib.add(-5, -3)
        self.assertEqual(result_neg_operands, -8)

        result_pos_neg_operands_1 = math_lib.add(-10, 5)
        self.assertEqual(result_pos_neg_operands_1, -5)

        result_pos_neg_operands_2 = math_lib.add(-15, 20)
        self.assertEqual(result_pos_neg_operands_2, 5)

        result_zero = math_lib.add(42, 0)
        self.assertEqual(result_zero, 42)

        result_neg_zero = math_lib.add(-42, 0)
        self.assertEqual(result_neg_zero, -42)

    ## Set of tests for subtraction
    #  @param self The object pointer.
    def test_sub(self):
        result_pos_operands_1 = math_lib.sub(2, 7)
        self.assertEqual(result_pos_operands_1, -5)

        result_pos_operands_2 = math_lib.sub(5, 3)
        self.assertEqual(result_pos_operands_2, 2)

        result_pos_neg_operands_1 = math_lib.sub(-10, -5)
        self.assertEqual(result_pos_neg_operands_1, -5)

        result_pos_neg_operands_2 = math_lib.sub(-15, -20)
        self.assertEqual(result_pos_neg_operands_2, 5)

        result_zero = math_lib.sub(33, 0)
        self.assertEqual(result_zero, 33)

        result_neg_zero = math_lib.sub(-33, 0)
        self.assertEqual(result_neg_zero, -33)

    ## Set of tests for multiplication
    #  @param self The object pointer.
    def test_mult(self):
        result_pos_operands = math_lib.mult(2, 7)
        self.assertEqual(result_pos_operands, 14)

        result_neg_operands = math_lib.mult(-2, -14)
        self.assertEqual(result_neg_operands, 28)

        result_pos_neg_operands_1 = math_lib.mult(10, -5)
        self.assertEqual(result_pos_neg_operands_1, -50)

        result_pos_neg_operands_2 = math_lib.mult(-15, 3)
        self.assertEqual(result_pos_neg_operands_2, -45)

        result_zero = math_lib.mult(33, 0)
        self.assertEqual(result_zero, 0)

        result_neg_zero = math_lib.mult(-33, 0)
        self.assertEqual(result_neg_zero, 0)

    ## Set of tests for division
    #  @param self The object pointer.
    def test_div(self):
        result_pos_operands = math_lib.div(6, 3)
        self.assertEqual(result_pos_operands, 2)

        result_neg_operands = math_lib.div(-14, -2)
        self.assertEqual(result_neg_operands, 7)

        result_pos_neg_operands_1 = math_lib.div(10, -5)
        self.assertEqual(result_pos_neg_operands_1, -2)

        result_pos_neg_operands_2 = math_lib.div(-15, 3)
        self.assertEqual(result_pos_neg_operands_2, -5)

        result_pos_zero = math_lib.div(0, 33)
        self.assertEqual(result_pos_zero, 0)

        result_neg_zero = math_lib.div(0, -33)
        self.assertEqual(result_neg_zero, 0)

        with self.assertRaises(math_lib.DivByZeroException):
            math_lib.div(33, 0)
            math_lib.div(-33, 0)

    ## Set of tests for factorization
    #  @param self The object pointer.
    def test_fact(self):
        result_fact_5 = math_lib.fact(5)
        self.assertEqual(result_fact_5,120)
        result_fact_zero = math_lib.fact(0)
        self.assertEqual(result_fact_zero,1)
        with self.assertRaises(math_lib.DomainErrorException):
            result_fact_non_integer = math_lib.fact(2.5)
            math_lib.fact(-4)

    ## Set of tests for exponentiation
    #  @param self The object pointer.
    def test_expo(self):
        with self.assertRaises(math_lib.DomainErrorException):
            math_lib.exp(0, 0)
            math_lib.exp(4, 2.5)
            math_lib.exp(4, -2)
        result_expo_2_2 = math_lib.exp(2,2)
        self.assertEqual(result_expo_2_2,4)
        result_expo_4_3 = math_lib.exp(4, 3)
        self.assertEqual(result_expo_4_3, 64)


    ## Set of tests for root
    #  @param self The object pointer.
    def test_root(self):
        with self.assertRaises(math_lib.DomainErrorException):
            math_lib.root(2, -4)
            math_lib.root(0, 0)
        self.assertEqual(math_lib.root(4, 2), 2)
        self.assertEqual(math_lib.root(8, 3), 2)

    ## Test for modulo operation %
    #  @param self The object pointer.
    def test_mod(self):
        result_pos_operands = math_lib.mod(7, 7)
        self.assertEqual(result_pos_operands, 0)

        result_pos_operands = math_lib.mod(-100, 3)
        self.assertEqual(result_pos_operands, 2)

        result_pos_operands = math_lib.mod(7, 7)
        self.assertEqual(result_pos_operands, 0)

        result_pos_operands = math_lib.mod(20, 5)
        self.assertEqual(result_pos_operands, 0)

if __name__ == '__main__':
    unittest.main()