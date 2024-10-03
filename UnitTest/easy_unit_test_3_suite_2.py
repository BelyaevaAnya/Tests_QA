import unittest
import calc_script

class CalcTest(unittest.TestCase):
    def test_pow(self):
        """
        Test for function in calculator(a^b)
        :return:
        """
        self.assertEqual(calc_script.pow(1, 2), 1)

    def test_sqrt(self):
        """
        Test for function in calculator(^0.5)
        :return:
        """
        self.assertEqual(calc_script.sqrt(4), 2)
