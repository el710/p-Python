from runner import Runner
import unittest
from unittest import TestCase

class RunnerTest(TestCase):
    def test_walk(self):
        test_obj = Runner('tester1')
        for _ in range(10):
            test_obj.walk()
        
        self.assertEqual(test_obj.distance, 50)

    def test_run(self):
        test_obj = Runner('tester2')
        for _ in range(10):
            test_obj.run()
        
        self.assertEqual(test_obj.distance, 100)
    
    def test_challange(self):
        test_obj_1 = Runner('tester3')
        test_obj_2 = Runner('tester4')
        for _ in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    unittest.main()

