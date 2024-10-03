import unittest
import tests_12_3


RunnerToutnamentST = unittest.TestSuite()
# old vers
# calcST.addTest(unittest.makeSuite(easy_unit_test_2.CalcTest))
RunnerToutnamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunnerToutnamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerToutnamentST)