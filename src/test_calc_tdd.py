#TODO HLAVICKA



import unittest
import calc

## Documentation for a class.
#
#  More details.
class Test_calc(unittest.TestCase):

    ## Documentation for a method.
    #  @param self The object pointer.
    def test_plus(self):
        result = calc.math_lib.plus(7,7)
        self.assertEqual(result, 14)

