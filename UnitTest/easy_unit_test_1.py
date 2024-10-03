import calc_script
import unittest


class CalcTest(unittest.TestCase):
    def test_add(self):
        """
        Test for function in calculator
        :return:
        """
        self.assertEqual(calc_script.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc_script.sub(3, 2), 1)


if __name__ == '__main__':
    unittest.main()
