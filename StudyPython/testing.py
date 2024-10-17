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

import unittest
class CalcTest(unittest.TestCase):
    def test_add(self):
        """
            Test for add() from test_calc.py
            :return:
        """
        self.assertEqual(cft.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(cft.sub(5, 2), 3)

if __name__ == "__main__":
    unittest.main()

