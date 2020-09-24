import unittest
from simple_calculator import Calculator, fun
from math import sqrt
from random import randint
from  datetime import datetime


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(randint(1, 100000))

    def test_add(self):
        """
        Test add function with regular data
        :rtype: object
        """
        print('Start time: ', datetime.now().minute, 'm ', datetime.now().second, 's ', datetime.now().microsecond, 'ms')
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEquals(self.calculator.divide(2, 3).value, calc_value / 6)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(4).root(2).value, calc_value**2)

    def test_power_zero(self):
        calc_value = 0
        self.calculator.value = 0
        self.assertEqual(self.calculator.power(5).root(7).value, 0)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2).value, sqrt(calc_value))
        print('End time: ', datetime.now().minute, 'm ', datetime.now().second, 's ', datetime.now().microsecond, 'ms')

    def test_all(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(6, 3, 1, 9, 4).root(8).add(6, 2, 1).divide(4, 5).value, (sqrt(sqrt(sqrt(calc_value*648)))+9)/20)


if __name__ == '__main__':
    unittest.main()


