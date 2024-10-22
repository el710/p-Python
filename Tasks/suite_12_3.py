"""
    TestSuite file...
"""
import unittest
import tests_12_3

com_test_suite = unittest.TestSuite()

com_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
com_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(com_test_suite)