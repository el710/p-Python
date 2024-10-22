"""
Testing...
import test_12*.py
"""

"""
idea of unit-test
"""
import calc_for_test as cft

def test_add():
    if cft.add(1, 2) == 3:
        print(f"add(): is ok")
    else:
        print(f"add(): is fail")

def test_sub():
    if cft.sub(5, 2) == 3:
        print(f"sub(): is ok")
    else:
        print(f"sub(): is fail")

def test_mul():
    if cft.mul(5, 2) == 10:
        print(f"mul(): is ok")
    else:
        print(f"mul(): is fail")

def test_div():
    if cft.div(6, 2) == 3.:
        print(f"div(): is ok")
    else:
        print(f"div(): is fail")

test_add()
test_sub()
test_mul()
test_div()

################################################
print("\nUnit-test style...\n")

"""
embedded framework <unittest> build tests in dev environment
"""
import unittest 
import random

"""
TestCase - class, the one whose test-methods will called by main() function of <unitest>
All TestCase descendants grouped in 'TestSuite' - set of TestCases
"""
## make new TestCase-type class with set of tests...
class CalcTest(unittest.TestCase):
    """
        setUpClass() will called once, before all test methods - like global initialization
        with decorator <@classmethod>
    """
    @classmethod
    def setUpClass(cls):
        print("setUpClass(): start testing...")

    """
        setUp() will called automatically before each test method - prolog
    """
    def setUp(self) -> None:
        ##super().setUp()
        print("setUp() run test N...")
    
    """
        tearDown() will called after each test - epilog
    """
    def tearDown(self):
        print('tearDown(): N  test is over')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass(): All tests are finished')

    """
     test method - called 'fixture'
    """
    def test_add(self):
        """
            Test for add() from test_calc.py
            :return:
        """
        self.assertEqual(cft.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(cft.sub(5, 2), 3)

    def test_assertions(self):
        self.assertNotEqual(7, 5) ## are they not equal :)
        self.assertAlmostEqual(3.22, 3.22) ## this for real variables means 7 digits after point
        self.assertTrue(True)
        self.assertIs('me', 'me')
        self.assertIsNone(None)
        self.assertIn('b', 'abc')
        self.assertRaises(expected_exception=TypeError) ## was there any exception
        self.assertWarns(expected_warning=Warning) ## was there any warning
        self.assertLess(5, 7)
        self.assertLessEqual(5, 5)
    
    """
        methods to skip some tests temporary...
    """
    @unittest.skip("becouse it's double test...")
    def test_double(self):
        pass

    @unittest.skipIf(random.randint(0, 2), "becouse only for odd testings...")
    def test_odd(self):
        pass



if __name__ == "__main__":
    ## start main process of testing
    unittest.main()

