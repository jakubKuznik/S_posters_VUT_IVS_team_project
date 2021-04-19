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
import calc


## Documentation for a class.
#
#  Unit Test for basic mathematical operation e.g. addition
#  subtraction, multiplication, division.


class TestBasicOperations(unittest.TestCase):
    ## Set of tests for addition
    #  @param self The object pointer.
    def test_add(self):
        result_pos_operands = calc.math_lib.add(7, 7)
        self.assertEqual(result_pos_operands, 14)

        result_neg_operands = calc.math_lib.add(-5, -3)
        self.assertEqual(result_neg_operands, -8)

        result_pos_neg_operands_1 = calc.math_lib.add(-10, 5)
        self.assertEqual(result_pos_neg_operands_1, -5)

        result_pos_neg_operands_2 = calc.math_lib.add(-15, 20)
        self.assertEqual(result_pos_neg_operands_2, 5)

        result_zero = calc.math_lib.add(42, 0)
        self.assertEqual(result_zero, 42)

        result_neg_zero = calc.math_lib.add(-42, 0)
        self.assertEqual(result_neg_zero, -42)

    ## Set of tests for subtraction
    #  @param self The object pointer.
    def test_sub(self):
        result_pos_operands_1 = calc.math_lib.sub(2, 7)
        self.assertEqual(result_pos_operands_1, -5)

        result_pos_operands_2 = calc.math_lib.sub(5, 3)
        self.assertEqual(result_pos_operands_2, 2)

        result_pos_neg_operands_1 = calc.math_lib.sub(-10, -5)
        self.assertEqual(result_pos_neg_operands_1, -5)

        result_pos_neg_operands_2 = calc.math_lib.sub(-15, -20)
        self.assertEqual(result_pos_neg_operands_2, 5)

        result_zero = calc.math_lib.sub(33, 0)
        self.assertEqual(result_zero, 33)

        result_neg_zero = calc.math_lib.sub(-33, 0)
        self.assertEqual(result_neg_zero, -33)

    ## Set of tests for multiplication
    #  @param self The object pointer.
    def test_mult(self):
        result_pos_operands = calc.math_lib.mult(2, 7)
        self.assertEqual(result_pos_operands, 14)

        result_neg_operands = calc.math_lib.mult(-2, -14)
        self.assertEqual(result_neg_operands, 28)

        result_pos_neg_operands_1 = calc.math_lib.mult(10, -5)
        self.assertEqual(result_pos_neg_operands_1, -50)

        result_pos_neg_operands_2 = calc.math_lib.mult(-15, 3)
        self.assertEqual(result_pos_neg_operands_2, -45)

        result_zero = calc.math_lib.mult(33, 0)
        self.assertEqual(result_zero, 0)

        result_neg_zero = calc.math_lib.mult(-33, 0)
        self.assertEqual(result_neg_zero, 0)

    ## Set of tests for division
    #  @param self The object pointer.
    def test_div(self):
        result_pos_operands = calc.math_lib.div(6, 3)
        self.assertEqual(result_pos_operands, 2)

        result_neg_operands = calc.math_lib.div(-14, -2)
        self.assertEqual(result_neg_operands, 7)

        result_pos_neg_operands_1 = calc.math_lib.div(10, -5)
        self.assertEqual(result_pos_neg_operands_1, -2)

        result_pos_neg_operands_2 = calc.math_lib.div(-15, 3)
        self.assertEqual(result_pos_neg_operands_2, -5)

        result_pos_zero = calc.math_lib.div(0, 33)
        self.assertEqual(result_pos_zero, 0)

        result_neg_zero = calc.math_lib.div(0, -33)
        self.assertEqual(result_neg_zero, 0)

        with self.assertRaises(calc.math_lib.DivByZero):
            calc.math_lib.div(33, 0)
            calc.math_lib.div(-33, 0)

    ## Set of tests for factorization
    #  @param self The object pointer.
    def test_fact(self):
        result_fact_5 = calc.math_lib.fact(5)
        self.assertEqual(result_fact_5,120)
        result_fact_zero = calc.math_lib.fact(0)
        self.assertEqual(result_fact_zero,1)
        with self.assertRaises(calc.math_lib.DomainError):
            result_fact_non_integer = calc.math_lib.fact(2.5)
            calc.math_lib.fact(-4)

    ## Set of tests for exponentiation
    #  @param self The object pointer.
    def test_expo(self):
        with self.assertRaises(calc.math_lib.DomainError):
            calc.math_lib.exponentiation(0, 0)
            calc.math_lib.exponentiation(4, 2.5)
            calc.math_lib.exponentiation(4, -2)
        result_expo_2_2 = calc.math_lib.exponentiation(2,2)
        self.assertEqual(result_expo_2_2,4)
        result_expo_4_3 = calc.math_lib.exponentiation(4, 3)
        self.assertEqual(result_expo_4_3, 64)


    ## Set of tests for root
    #  @param self The object pointer.
    def test_root(self):
        with self.assertRaises(calc.math_lib.DomainError):
            calc.math_lib.root(2, -4)
            calc.math_lib.root(0, 0)
        result_root_2_4 = calc.math_lib.root(2, 4)
        self.assertEqual(result_root_2_4, 2)
        result_root_3_neg8 = calc.math_lib.root(3, -8)
        self.assertEqual(result_root_3_neg8, -2)

    ## Test for modulo operation %
    #  @param self The object pointer.
    def test_modulo(self):
        result_pos_operands = calc.math_lib.modulo(7, 7)
        self.assertEqual(result_pos_operands, 0)

        result_pos_operands = calc.math_lib.modulo(-100, 3)
        self.assertEqual(result_pos_operands, 2)

        result_pos_operands = calc.math_lib.modulo(7, 7)
        self.assertEqual(result_pos_operands, 0)

        result_pos_operands = calc.math_lib.modulo(20, 5)
        self.assertEqual(result_pos_operands, 0)



