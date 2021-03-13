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

## @file test_calc_tdd.py
#
#  @brief tests

import unittest
import calc

## Documentation for a class.
#
#  More details.


class TestCalc(unittest.TestCase):
    ## Documentation for a method.
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
