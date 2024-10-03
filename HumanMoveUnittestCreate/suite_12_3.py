import unittest
import tests_12_3


RunnerToutnamentST = unittest.TestSuite()
# old vers
# calcST.addTest(unittest.makeSuite(easy_unit_test_2.CalcTest))
RunnerToutnamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunnerToutnamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerToutnamentST)
#
# test_challange (tests_12_3.RunnerTest.test_challange) ... ok
# test_false_run (tests_12_3.RunnerTest.test_false_run) ... FAIL
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_race_all (tests_12_3.TournamentTest.test_race_all) ... skipped 'Тесты в этом кейсе заморожены'
# test_race_andrey_and_nick (tests_12_3.TournamentTest.test_race_andrey_and_nick) ... skipped 'Тесты в этом кейсе заморожены'
# test_race_usain_and_nick (tests_12_3.TournamentTest.test_race_usain_and_nick) ... skipped 'Тесты в этом кейсе заморожены'
#
# ======================================================================
# Тест заведомо ложный
# FAIL: test_false_run (tests_12_3.RunnerTest.test_false_run)
# ----------------------------------------------------------------------