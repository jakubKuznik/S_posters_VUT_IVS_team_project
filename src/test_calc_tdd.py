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
# Brief:
###########################################

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
