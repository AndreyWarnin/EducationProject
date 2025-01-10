from unittest import TestCase
import HumanMoveTest.runner_and_tournament as rat


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        runner1 = rat.Runner('Усэйн', 10)
        runner2 = rat.Runner('Андрей', 9)
        runner3 = rat.Runner('Ник', 3)
        self.runners = (runner1, runner2, runner3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            for item in results.items():
                print(item[0], item[1])


    def test_start_1(self):
        participants = (self.runners[0], self.runners[2])
        tournament = rat.Tournament(90, *participants)
        results = tournament.start()
        self.all_results[len(self.all_results.items())] = results
        self.assertTrue(results[2] == self.runners[2], f'Последний бегун: {results[2]}')

    def test_start_2(self):
        participants = (self.runners[1], self.runners[2])
        tournament = rat.Tournament(90, *participants)
        results = tournament.start()
        self.all_results[len(self.all_results.items())] = results
        self.assertTrue(results[2] == self.runners[2], f'Последний бегун: {results[2]}')

    def test_start_3(self):
        tournament = rat.Tournament(90, *self.runners)
        results = tournament.start()
        self.all_results[len(self.all_results.items())] = results
        self.assertTrue(results[3] == self.runners[2], f'Последний бегун: {results[3]}')

    def test_start_4(self):
        tournament = rat.Tournament(3, *self.runners)
        results = tournament.start()
        self.all_results[len(self.all_results.items())] = results
        self.assertTrue(results[3] == self.runners[2], f'Последний бегун: {results[3]}')

