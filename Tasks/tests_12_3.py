"""
    TestCase file ...
"""
import unittest
from unittest import TestCase
import runner_and_tournament
from runner_and_tournament import Runner, Tournament
from pprint import pprint


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_walk(self):
        test_obj = Runner('tester1')
        for _ in range(10): 
            test_obj.walk()
        self.assertEqual(test_obj.distance, 50)

    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_run(self):
        test_obj = Runner('tester2')
        for _ in range(10):
            test_obj.run()
        
        self.assertEqual(test_obj.distance, 100)
    
    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_challange(self):
        test_obj_1 = Runner('tester3')
        test_obj_2 = Runner('tester4')
        for _ in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass(): let's start testing")
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Usein', 10)
        self.runner_2 = Runner('Andrew', 9)
        self.runner_3 = Runner('Nick', 3)
        
    @classmethod
    def tearDownClass(cls) -> None:
        for item in cls.all_results:
            print(item)
        print("tearDownClass(): testing is over")
    
    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_tour1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[0][ind]=='Nick')

    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_tour2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[1][ind]=='Nick')

    @unittest.skipIf(is_frozen == True, "Tests in that Case are frozen")
    def test_tour3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[2][ind]=='Nick')

if __name__ == '__main__':
    unittest.main()

