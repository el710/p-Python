import unittest
import calc_for_test as cft

"""
other tests file for TestSuite....
"""

class NewTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(cft.sqrt(4), 2)
    
    def test_pow(self):
        self.assertNotEqual(cft.pow(3, 3), 26)
    

if __name__ == "__main__":
    unittest.main()