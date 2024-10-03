import calc_script
import unittest


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

    def test_add(self):
        """
        Test for function in calculator(+)
        :return:
        """
        self.assertEqual(calc_script.add(1, 2), 3)

    def test_sub(self):
        """
        Test for function in calculator(-)
        :return:
        """
        self.assertEqual(calc_script.sub(3, 2), 1)

    def test_test(self):
        # self.assertNotRegex()
        pass

if __name__ == '__main__':
    unittest.main()
