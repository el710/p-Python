import unittest
from unittest import TestCase
import runner_and_tournament
from runner_and_tournament import Runner, Tournament
from pprint import pprint


class TournamentTest(TestCase):

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
        print("tearDownClass(): testing is over")
        for item in cls.all_results:
            print(item)

    
    def test_tour1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[0][ind]=='Nick')

    def test_tour2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[1][ind]=='Nick')

    def test_tour3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res = tournament.start()
        ind = len(res)
        TournamentTest.all_results.append(res)    
        self.assertTrue(TournamentTest.all_results[2][ind]=='Nick')

   

if __name__ == '__main__':
    unittest.main()


