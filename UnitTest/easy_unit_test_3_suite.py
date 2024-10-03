import unittest
import easy_unit_test_2
import easy_unit_test_3_suite_2

calcST = unittest.TestSuite()
# old vers
# calcST.addTest(unittest.makeSuite(easy_unit_test_2.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(easy_unit_test_2.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(easy_unit_test_3_suite_2.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)