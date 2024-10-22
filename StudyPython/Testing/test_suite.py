import unittest
import testing
import test_new

"""
make object of class TestSuite
"""
calc_test_suite = unittest.TestSuite()

"""
add tests from TestCase class...
"""
# calc_test_suite.addSubTest(unittest.makeSuite(testing.CalcTest)) ## old fasion call
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testing.CalcTest))

## add from other test file - test_new.py
calc_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new.NewTest))

"""
make runner to config and run TestSuite...
"""
##                               verbosity - is a level of detailization    
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calc_test_suite)