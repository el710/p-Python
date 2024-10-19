"""
Testing...
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

"""
TestCase - class, which test-methods will called by main() function of <unitest>
All TestCase classes(objects) make out 'TestSuite' - set of TestCases
"""
## make new TestCase-type class with set of tests...
class CalcTest(unittest.TestCase):
    """
        setUpClass() will called once before all test methods - like global initialization
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
        print("setup() run test N...")
    
    """
        tearDown() will called after each test - epilog
    """
    def tearDown(self):
        print('tearDown(): after test start tearDown()')

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
        self.assertAlmostEqual(3.21, 3.22) ## this for real variables means 7 digits after point
        self.assertTrue(False)
        self.assertIs('me', 'me')
        self.assertIsNone(None)
        self.assertIn('b', 'abc')
        self.assertRaises() ## was there any exception
        self.assertWarns() ## was there any warning
        self.assertLess(5, 7)
        self.assertLessEqual(5, 5)


if __name__ == "__main__":
    ## start main process of testing
    unittest.main()

