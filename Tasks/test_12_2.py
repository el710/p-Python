import unittest
from unittest import TestCase
import runner_and_tournament
from runner_and_tournament import Runner, Tournament
from pprint import pprint


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass(): let's start testing")
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Usein', 10)
        self.runner_2 = Runner('Andrew', 9)
        self.runner_3 = Runner('Nick', 3)
        
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass(): testing is over")


    def tearDown(self):
        for item in TournamentTest.all_results:
            print(item, TournamentTest.all_results[item])
    
    def test_tour1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results = tournament.start()
        print('\n', TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results, 'Nick')

    def test_tour2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results = tournament.start()
        print('\n', TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results, 'Nick')

    def test_tour3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results = tournament.start()
        print('\n', TournamentTest.all_results)
        self.assertTrue(TournamentTest.all_results, 'Nick')

   

if __name__ == '__main__':
    unittest.main()


