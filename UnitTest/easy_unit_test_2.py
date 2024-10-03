import calc_script
import unittest
import random


class CalcTest(unittest.TestCase):
    def setUp(self):
        print('Setup')

    @classmethod
    def setUpClass(cls):
        print('MegaSetup')

    def tearDown(self):
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    @unittest.skip("Временное исключение теста")
    def test_add(self):
        """
        Test for function in calculator(+)
        :return:
        """
        self.assertEqual(calc_script.add(1, 2), 3)

    def test_div(self):
        """
        Test for function in calculator(/)
        :return:
        """
        self.assertEqual(calc_script.div(4, 2), 2)

    @unittest.skipIf(random.randint(0, 2), reason='Не повезло')
#       @unittest.skipIf(False, reason='Не повезло')-тест идет
#       @unittest.skipIf(True, reason='Не повезло')-тест не идет
    def test_sub(self):
        """
        Test for function in calculator(-)
        :return:
        """
        self.assertEqual(calc_script.sub(3, 2), 1)

    def test_mul(self):
        """
        Test for function in calculator(*)
        :return:
        """
        self.assertEqual(calc_script.mul(5, 2), 10)

    def test_test(self):
        # self.assertNotRegex()
        pass


if __name__ == '__main__':
    unittest.main()
