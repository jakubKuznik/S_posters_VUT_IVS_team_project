# ##########################################
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
# ##########################################

## Tests for math_lib and calc_parser
#
#  @package test_calc_tdd
#  @file test_calc_tdd.py
#
#  @author Vaňo Michal
#  @author Kuzník Jakub
#  @author Kratochvíl Pavel
#  @author Svobodová Lucie

import unittest
import math_lib
import calc_parser

## 
#  Unit Test for basic mathematical operation e.g. addition
#  subtraction, multiplication, division.
class TestBasicOperations(unittest.TestCase):

    ## Set of tests for addition
    #  @param self The object pointer.
    def test_add(self):
        # testing positive operands
        result_pos_operands = math_lib.add(7, 7)
        self.assertEqual(14, result_pos_operands)
        
        result_pos_operands = math_lib.add(2434, 743)
        self.assertEqual(3177, result_pos_operands)
        
        result_pos_operands = math_lib.add(1835.74, 27)
        self.assertEqual(1862.74, result_pos_operands)
        
        result_pos_operands = math_lib.add(100, 100)
        self.assertEqual(200, result_pos_operands)

        # testing negative operands
        result_neg_operands = math_lib.add(-5, -3)
        self.assertEqual(-8, result_neg_operands)

        result_neg_operands = math_lib.add(-648, -63)
        self.assertEqual(-711, result_neg_operands)

        result_neg_operands = math_lib.add(-9.15, -157.95)
        self.assertEqual(-167.1, result_neg_operands)

        result_neg_operands = math_lib.add(-100, -1000)
        self.assertEqual(-1100, result_neg_operands)

        # testing first operand positive and second one negative
        result_pos_neg_operands = math_lib.add(10, -5)
        self.assertEqual(5, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.add(0, -485.7)
        self.assertEqual(-485.7, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.add(18, -4)
        self.assertEqual(14, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.add(66, -666)
        self.assertEqual(-600, result_pos_neg_operands)

        # testing first operand negative and second operand positive
        result_neg_pos_operands = math_lib.add(-15, 20)
        self.assertEqual(5, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.add(-35, 2.14)
        self.assertEqual(-32.86, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.add(-23, 845)
        self.assertEqual(822, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.add(-1057, 207)
        self.assertEqual(-850, result_neg_pos_operands)

        # testing operands that returns zero
        result_zero = math_lib.add(42, -42)
        self.assertEqual(0, result_zero)

        result_zero = math_lib.add(-23.8, 23.8)
        self.assertEqual(0, result_zero)
        
        result_zero = math_lib.add(0, 0)
        self.assertEqual(0, result_zero)

        result_not_zero = math_lib.add(-4219, 421)
        self.assertNotEqual(0, result_not_zero)


    ## Set of tests for subtraction
    #  @param self The object pointer.
    def test_sub(self):
        # testing positive operands
        result_pos_operands = math_lib.sub(2, 7)
        self.assertEqual(-5, result_pos_operands)

        result_pos_operands = math_lib.sub(95, 71.5)
        self.assertEqual(23.5, result_pos_operands)

        result_pos_operands = math_lib.sub(4786, 7)
        self.assertEqual(4779, result_pos_operands)

        result_pos_operands = math_lib.sub(25, 778)
        self.assertEqual(-753, result_pos_operands)
        
        # testing negative operands
        result_neg_operands = math_lib.sub(-5, -3)
        self.assertEqual(-2, result_neg_operands)

        result_neg_operands = math_lib.sub(-255.784, -73)
        self.assertEqual(-182.784, result_neg_operands)

        result_neg_operands = math_lib.sub(-5, -83)
        self.assertEqual(78, result_neg_operands)

        result_neg_operands = math_lib.sub(-5885, -393)
        self.assertEqual(-5492, result_neg_operands)

        # testing first operand positive and second one negative
        result_pos_neg_operands = math_lib.sub(10, -841)
        self.assertEqual(851, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.sub(810, -1.451)
        self.assertEqual(811.451, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.sub(1, -25)
        self.assertEqual(26, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.sub(774, -5)
        self.assertEqual(779, result_pos_neg_operands)

        # testing first operand negative and second operand positive
        result_neg_pos_operands = math_lib.sub(-15, 20)
        self.assertEqual(-35, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.sub(-83.4, 70.6)
        self.assertEqual(-154, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.sub(-7615, 234)
        self.assertEqual(-7849, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.sub(-97, 1)
        self.assertEqual(-98, result_neg_pos_operands)

        # testing operands that returns zero
        result_zero = math_lib.sub(33, 33)
        self.assertEqual(0, result_zero)

        result_zero = math_lib.sub(-854, -854)
        self.assertEqual(0, result_zero)

        result_zero = math_lib.sub(0, 0)
        self.assertEqual(0, result_zero)

        result_not_zero = math_lib.sub(-73, 0)
        self.assertNotEqual(result_not_zero, 0)


    ## Set of tests for multiplication
    #  @param self The object pointer.
    def test_mult(self):
        # testing positive operands
        result_pos_operands = math_lib.mult(2, 7)
        self.assertEqual(14, result_pos_operands)

        result_pos_operands = math_lib.mult(547, 31)
        self.assertEqual(16957, result_pos_operands)

        result_pos_operands = math_lib.mult(9, 467)
        self.assertEqual(4203, result_pos_operands)

        result_pos_operands = math_lib.mult(964.78, 10)
        self.assertEqual(9647.8, result_pos_operands)

        # testing negative operands
        result_neg_operands = math_lib.mult(-2, -14)
        self.assertEqual(28, result_neg_operands)

        result_neg_operands = math_lib.mult(-64, -9)
        self.assertEqual(576, result_neg_operands)

        result_neg_operands = math_lib.mult(-4, -6728)
        self.assertEqual(26912, result_neg_operands)

        result_neg_operands = math_lib.mult(-2148, -548.7)
        self.assertEqual(1178607.6, result_neg_operands)

        # testing first operand positive and second one negative
        result_pos_neg_operands = math_lib.mult(10, -5)
        self.assertEqual(-50, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.mult(61.0, -2)
        self.assertEqual(-122.0, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.mult(1, -548)
        self.assertEqual(-548, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.mult(100, -41)
        self.assertEqual(-4100, result_pos_neg_operands)

        # testing first operand negative and second operand positive
        result_neg_pos_operands = math_lib.mult(-10, 5)
        self.assertEqual(-50, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.mult(-84, 73.4)
        self.assertEqual(-6165.6, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.mult(-457, 1)
        self.assertEqual(-457, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.mult(-111, 111)
        self.assertEqual(-12321, result_neg_pos_operands)

        # testing operands that returns zero
        result_zero = math_lib.mult(33, 0)
        self.assertEqual(0, result_zero)

        result_zero = math_lib.mult(0, 40.4)
        self.assertEqual(0, result_zero)

        result_zero = math_lib.mult(0, 0)
        self.assertEqual(0, result_zero)

        result_not_zero = math_lib.mult(-1, 1)
        self.assertNotEqual(result_not_zero, 0)


    ## Set of tests for division
    #  @param self The object pointer.
    def test_div(self):
        # testing positive operands
        result_pos_operands = math_lib.div(6, 3)
        self.assertEqual(2, result_pos_operands)

        result_pos_operands = math_lib.div(74.8, 25)
        self.assertEqual(2.992, result_pos_operands)

        result_pos_operands = math_lib.div(845, 65)
        self.assertEqual(13, result_pos_operands)

        result_pos_operands = math_lib.div(12.4, 0.2)
        self.assertEqual(62, result_pos_operands)

        # testing negative operands
        result_neg_operands = math_lib.div(-14, -2)
        self.assertEqual(7, result_neg_operands)

        result_neg_operands = math_lib.div(-4, -2)
        self.assertEqual(2, result_neg_operands)

        result_neg_operands = math_lib.div(-0.5, -2)
        self.assertEqual(0.25, result_neg_operands)

        result_neg_operands = math_lib.div(-64.5, -3)
        self.assertEqual(21.5, result_neg_operands)

        # testing first operand positive and second one negative
        result_pos_neg_operands = math_lib.div(10, -5)
        self.assertEqual(-2, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.div(14, -0.5)
        self.assertEqual(-28, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.div(10.5, -6)
        self.assertEqual(-1.75, result_pos_neg_operands)

        result_pos_neg_operands = math_lib.div(10, -200)
        self.assertEqual(-0.05, result_pos_neg_operands)

        # testing first operand negative and second operand positive
        result_neg_pos_operands = math_lib.div(-54, 6)
        self.assertEqual(-9, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.div(-154.5, 1.2)
        self.assertEqual(-128.75, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.div(-84, 7.5)
        self.assertEqual(-11.2, result_neg_pos_operands)

        result_neg_pos_operands = math_lib.div(-15, 3)
        self.assertEqual(-5, result_neg_pos_operands)

        # testing operands that returns zero
        result_pos_zero = math_lib.div(0, 33)
        self.assertEqual(result_pos_zero, 0)

        result_pos_zero = math_lib.div(0, -87)
        self.assertEqual(result_pos_zero, 0)

        result_not_zero = math_lib.div(14, -14)
        self.assertNotEqual(result_not_zero, 0)

        # testing errors
        result_error = math_lib.div(33, 0)
        self.assertEqual("Math Error", result_error)
        
        result_error = math_lib.div(-73, 0)
        self.assertEqual("Math Error", result_error)
        
        result_error = math_lib.div(2.5, 0)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.div(0, 0)
        self.assertEqual("Math Error", result_error)

    ## Set of tests for factorization
    #  @param self The object pointer.
    def test_fact(self):
        # testing positive operands
        result_fact_pos = math_lib.fact(1)
        self.assertEqual(1, result_fact_pos)
        
        result_fact_pos = math_lib.fact(5)
        self.assertEqual(120, result_fact_pos)
        
        result_fact_pos = math_lib.fact(9)
        self.assertEqual(362880, result_fact_pos)
        
        # testing zero
        result_fact_zero = math_lib.fact(0)
        self.assertEqual(1, result_fact_zero)

        # testing errors
        result_error = math_lib.fact(2.5)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.fact(-44)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.fact(-2.35)
        self.assertEqual("Math Error", result_error)


    ## Set of tests for exponentiation
    #  @param self The object pointer.
    def test_exp(self):
        # testing positive operands
        result_exp_pos = math_lib.exp(2, 2)
        self.assertEqual(4, result_exp_pos)

        result_exp_pos = math_lib.exp(25, 3)
        self.assertEqual(15625, result_exp_pos)

        result_exp_pos = math_lib.exp(2, 8)
        self.assertEqual(256, result_exp_pos)

        result_exp_pos = math_lib.exp(6, 0)
        self.assertEqual(1, result_exp_pos)

        # testing negative operands
        result_exp_neg = math_lib.exp(-4, -3)
        self.assertEqual(-0.015625, result_exp_neg)

        result_exp_neg = math_lib.exp(-5, -1)
        self.assertEqual(-0.2, result_exp_neg)

        result_exp_neg = math_lib.exp(-0.5, -2)
        self.assertEqual(4, result_exp_neg)

        result_exp_neg = math_lib.exp(-1, -30)
        self.assertEqual(1, result_exp_neg)

        # testing first operand positive and second one negative
        result_exp_pos_neg = math_lib.exp(4, -2)
        self.assertEqual(0.0625, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.exp(2, -1)
        self.assertEqual(0.5, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.exp(2, -3)
        self.assertEqual(0.125, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.exp(1, -2)
        self.assertEqual(1, result_exp_pos_neg)

        # testing first operand negative and second operand positive
        result_exp_neg_pos = math_lib.exp(-4, 2)
        self.assertEqual(16, result_exp_neg_pos)
        
        result_exp_neg_pos = math_lib.exp(-2, 8)
        self.assertEqual(256, result_exp_neg_pos)
        
        result_exp_neg_pos = math_lib.exp(-42, 1)
        self.assertEqual(-42, result_exp_neg_pos)
        
        result_exp_neg_pos = math_lib.exp(-1, 2)
        self.assertEqual(1, result_exp_neg_pos)

        # testing operands that returns zero
        result_zero = math_lib.exp(0, 2)
        self.assertEqual(0, result_zero)
        
        result_zero = math_lib.exp(0, 4)
        self.assertEqual(0, result_zero)

        # testing errors      
        result_error = math_lib.exp(0, 0)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.exp(0, -2)
        self.assertEqual("Math Error", result_error)


    ## Set of tests for root
    #  @param self The object pointer.
    def test_root(self):
        # testing positive operands
        result_exp_pos = math_lib.root(27, 3)
        self.assertEqual(3, result_exp_pos)

        result_exp_pos = math_lib.root(100, 2)
        self.assertEqual(10, result_exp_pos)

        result_exp_pos = math_lib.root(144, 2)
        self.assertEqual(12, result_exp_pos)

        result_exp_pos = math_lib.root(0, 3)
        self.assertEqual(0, result_exp_pos)

        # testing negative operands
        result_exp_neg = math_lib.root(-8, -3)
        self.assertEqual(-0.5, result_exp_neg)

        result_exp_neg = math_lib.root(-1024, -5)
        self.assertAlmostEqual(-0.25, result_exp_neg)

        # testing first operand positive and second one negative
        result_exp_pos_neg = math_lib.root(1024, -2)
        self.assertEqual(0.03125, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.root(8, -3)
        self.assertEqual(0.5, result_exp_pos_neg)

        # testing first operand negative and second operand positive
        result_exp_neg_pos = math_lib.root(-64, 3)
        self.assertAlmostEqual(-4, result_exp_neg_pos)        
        
        result_exp_neg_pos = math_lib.root(-78125, 7)
        self.assertAlmostEqual(-5, result_exp_neg_pos)        
        
        # testing operands that returns zero
        result_error = math_lib.root(-4, 2)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.root(0, 0)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.root(-455, 0)
        self.assertEqual("Math Error", result_error)


    ## Test for modulo operation %
    #  @param self The object pointer.
    def test_mod(self):
        # testing positive operands
        result_pos_operands = math_lib.mod(7, 7)
        self.assertEqual(0, result_pos_operands)
        
        result_pos_operands = math_lib.mod(13, 5)
        self.assertEqual(3, result_pos_operands)
        
        result_pos_operands = math_lib.mod(1, 3)
        self.assertEqual(1, result_pos_operands)
        
        result_pos_operands = math_lib.mod(158, 8)
        self.assertEqual(6, result_pos_operands)
        
        # testing negative operands
        result_neg_operands = math_lib.mod(-100, -3)
        self.assertEqual(-1, result_neg_operands)

        result_neg_operands = math_lib.mod(-1, -8)
        self.assertEqual(-1, result_neg_operands)

        result_neg_operands = math_lib.mod(-8, -3)
        self.assertEqual(-2, result_neg_operands)

        result_neg_operands = math_lib.mod(-57, -6)
        self.assertEqual(-3, result_neg_operands)

        # testing first operand positive and second one negative
        result_exp_pos_neg = math_lib.mod(4, -3)
        self.assertEqual(-2, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.mod(8, -3)
        self.assertAlmostEqual(-1, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.mod(4, -3)
        self.assertEqual(-2, result_exp_pos_neg)

        result_exp_pos_neg = math_lib.mod(245, -85)
        self.assertEqual(-10, result_exp_pos_neg)

        # testing first operand negative and second operand positive
        result_exp_neg_pos = math_lib.mod(-4, 2)
        self.assertEqual(0, result_exp_neg_pos)        
        
        result_exp_neg_pos = math_lib.mod(-2, 8)
        self.assertEqual(6, result_exp_neg_pos)
        
        result_exp_neg_pos = math_lib.mod(-42, 13)
        self.assertEqual(10, result_exp_neg_pos)
        
        result_exp_neg_pos = math_lib.mod(-1, 2)
        self.assertEqual(1, result_exp_neg_pos)

        # testing operands that returns zero
        result_pos_operands = math_lib.mod(7, 7)
        self.assertEqual(0, result_pos_operands)

        result_pos_operands = math_lib.mod(20, 5)
        self.assertEqual(0, result_pos_operands)

        result_error = math_lib.mod(33, 0)
        self.assertEqual("Math Error", result_error)
        
        result_error = math_lib.mod(-73, 0)
        self.assertEqual("Math Error", result_error)
        
        result_error = math_lib.mod(2.5, 0)
        self.assertEqual("Math Error", result_error)

        result_error = math_lib.mod(0, 0)
        self.assertEqual("Math Error", result_error)

## 
#  Unit Test for parsing expressions
#
class TestParser(unittest.TestCase):

    ## Set of tests for one operation
    #  @param self The object pointer.
    def test_one_operation(self):
        # add
        result = calc_parser.split_string_fn(list("2+3"), list("2+3"))
        self.assertEqual(5, result)

        result = calc_parser.split_string_fn(list("458+45"), list("458+45"))
        self.assertEqual(503, result)
        
        # sub
        result = calc_parser.split_string_fn(list("74-8"), list("74-8"))
        self.assertEqual(66, result)
        
        result = calc_parser.split_string_fn(list("1-4965"), list("1-4965"))
        self.assertEqual(-4964, result)
        
        # mult
        result = calc_parser.split_string_fn(list("9*34"), list("9*34"))
        self.assertEqual(306, result)

        result = calc_parser.split_string_fn(list("873*0"), list("873*0"))
        self.assertEqual(0, result)
        
        # div
        result = calc_parser.split_string_fn(list("7/8"), list("7/8"))
        self.assertEqual(0.875, result)
        
        result = calc_parser.split_string_fn(list("1/5"), list("1/5"))
        self.assertEqual(0.2, result)

        # fact
        result = calc_parser.split_string_fn(['1', '!', '0'], list("1!"))
        self.assertEqual(1, result)

        result = calc_parser.split_string_fn(['5', '!', '0'], list("5!"))
        self.assertEqual(120, result)

        result = calc_parser.split_string_fn(['0', '!', '0'], list("0!"))
        self.assertEqual(1, result)

        # exp
        result = calc_parser.split_string_fn(['2', '&', '5'], list("2^5"))
        self.assertEqual(32, result)

        result = calc_parser.split_string_fn(['2', '5', '&', '3'], list("25^3"))
        self.assertEqual(15625, result)

        result = calc_parser.split_string_fn(['0', '&', '3'], list("0^3"))
        self.assertEqual(0, result)

        # root
        result = calc_parser.split_string_fn(['(', '27', ')', '$', '(', '3', ')'], list("[3]√(27)"))
        self.assertEqual(3, result)

        result = calc_parser.split_string_fn(['(', '256', ')', '$', '(', '-2.0', ')'], list("[-2]√(256)"))
        self.assertEqual(0.0625, result)

        # mod
        result = calc_parser.split_string_fn(['4', '5', '?', '6'], list("45mod6"))
        self.assertEqual(3, result)

        result = calc_parser.split_string_fn(['1', '2', '3', '?', '6', '5', '8'], list("123mod658"))
        self.assertEqual(123, result)

    ## Set of tests for expressions that should return Math Error
    #  @param self The object pointer.
    def test_math_errors(self):
        result = calc_parser.split_string_fn(list("1/0"), list("1/0"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(list("0/0"), list("0/0"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['36', '.', '5', '!', '0'], list("36.5!"))
        self.assertEqual("Math Error", result)
        
        result = calc_parser.split_string_fn(['(', '-', '4', '4', ')', '!', '0'], list("(-44)!"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['(', '-', '4', '.', '4', ')', '!', '0'], list("(-4.4)!"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['0', '&', '0'], list("0^0"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['0', '&', '(', '-', '6', ')'], list("0^(-6)"))
        self.assertEqual("Math Error", result)
        
        result = calc_parser.split_string_fn(['(', '0', ')', '$', '(', '0', ')'], list("[0]√(0)"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['(', '-64.0', ')', '$', '(', '-8.0', ')'], list("[-8]√(-64)"))
        self.assertEqual("Math Error", result)

        result = calc_parser.split_string_fn(['3', '3', '?', '0'], list("33mod0"))
        self.assertEqual("Math Error", result)

    ## Set of tests for parsing parentheses
    #  @param self The object pointer.
    def test_parentheses(self):
        result = calc_parser.split_string_fn(['(', '-', '4', ')', '&', '2'], list("(-4)^2"))
        self.assertEqual(16, result)

        result = calc_parser.split_string_fn(['4', '&', '(', '-', '2', ')'], list("4^(-2)"))
        self.assertEqual(0.0625, result)

        result = calc_parser.split_string_fn(['(', '-', '1', '2', '3', ')', '?', '6', '5', '8'], list("(-123)mod658"))
        self.assertEqual(535, result)

        result = calc_parser.split_string_fn(['(', '-', '4', ')', '?', '2'], list("(-4)mod2"))
        self.assertEqual(0, result)

    ## Set of tests for expressions that should return Syntax Error
    #  @param self The object pointer.
    def test_syntax_errors(self):
        result = calc_parser.split_string_fn(['2', '+', '&', '2'], list("2+^2"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['8', '(', '&', ')'], list("8(^)"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', '0', '*', '6'], list("2M*6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['7', '(', '0', ')'], list("(7)M"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['5', '(', '6', ')'], list("5(6)"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['6', '-', '(', '8'], list("6-(8"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', ')'], list("2)"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['(', '5', '-', ')', '+', '6'], list("(5-)+6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', '*', '-', '9'], list("2*-9"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['5', '8', '6', '*'], list("586*"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['1', '0', '0', '/', '-', '6'], list("100/-6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['/', '6'], list("/6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['!', '0'], list("!"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['/', '6'], list("/6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', '-', '!', '0'], list("2-!"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['-'], list("-"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['5', '*', '?', '6'], list("5*mod6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', '?'], list("2mod"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['+', '6', '9'], list("+69"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['2', '+', '(', '+', '9', ')'], list("2+(+9)"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['3.1415926535', '3.1415926535'], list("ππ"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['6', '.', '5', '.', '3'], list("6.5.3"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['.', '9', '6'], list(".96"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['5', '-', '.', '6'], list("5-.6"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['(', '256', ')', '$', '(', '2', ')', '9'], list("[2]√(256)9"))
        self.assertEqual("Syntax Error", result)

        result = calc_parser.split_string_fn(['4', '5', '(', '27', ')', '$', '(', '3', ')'], list("45[3]√(27)"))
        self.assertEqual("Syntax Error", result)
        

    def test_multiple_operations(self):
        result = calc_parser.split_string_fn(['5', '*', '(', '8', '-', '6', ')', '&', '(', '4', '/', '2', ')', '+', '(', '6', '?', '2', ')'], list("5*(8-6)^(4/2)+(6mod2)"))
        self.assertEqual(20, result)

        result = calc_parser.split_string_fn(['5', '6', '/', '9', '+', '5', '8', '1', '-', '6', '!', '0'], list("56/9+581-6!"))
        self.assertAlmostEqual(-132.77777777778, result)
        
        result = calc_parser.split_string_fn(['(', '25', '*', '9', ')', '$', '(', '1', '+', '3', '-', '4', ')'], list("[1+3-4]√(25*9)"))
        self.assertEqual("Math Error", result)
        
        result = calc_parser.split_string_fn(['(', '4', '&', '2', ')', '$', '(', '8', '*', '0', '.', '5', ')'], list("[8*0.5]√(4^2)"))
        self.assertEqual(2, result)

        result = calc_parser.split_string_fn(['5', '-', '(', '(', '8', '*', '9', ')', '/', '5', ')', '+', '(', '1', '/', '3.1415926535', ')', '*', '3.1415926535'], list("5-((8*9)/5)+(1/π)*π"))
        self.assertEqual(-8.4, result)

        result = calc_parser.split_string_fn(['5', '-', '(', '81', ')', '$', '(', '4', ')', '!', '0', '+', '(', '-', '6', ')', '&', '2', '-', '(', '1', '0', '0', '/', '5', '0', ')'], list("5-[4]√(81)!+(-6)^2-(100/50)"))
        self.assertEqual(33, result)

        result = calc_parser.split_string_fn(['3', '.', '2', '5', '8', '*', '4', '.', '2', '5', '+', '(', '8', '?', '6', '9', ')'], list("3.258*4.25+(8mod69)"))
        self.assertEqual(21.8465, result)

        result = calc_parser.split_string_fn(['8', '-', '(', '8', ')', '$', '(', '3', ')', '?', '2'], list("8-[3]√(8)mod2"))
        self.assertEqual(8, result)

        result = calc_parser.split_string_fn(['1', '4', '&', '(', '6', '*', '0', '.', '5', ')'], list("14^(6*0.5)"))
        self.assertEqual(2744, result)

        result = calc_parser.split_string_fn(['(', '7', '*', '(', '5', '8', '/', '2', ')', '-', '9', ')', '+', '(', '7', '-', '(', '-', '6', ')', ')'], list("(7*(58/2)-9)+(7-(-6))"))
        self.assertEqual(207, result)

        result = calc_parser.split_string_fn(['1', '4', '&', '(', '(', '4', ')', '$', '(', '2', ')', ')'], list("14^[2]√(4)"))
        self.assertEqual(196, result)


if __name__ == '__main__':
    unittest.main()