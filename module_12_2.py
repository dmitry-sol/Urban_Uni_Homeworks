import unittest
from unittest import TestCase


class Runner:

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

        # Ошибка в логике.
        # В каждый новый старт full_distance должна принимать исходное значение.
        # Поэтому должна объявляться внутри метода start.
        # Выявляется дополнительными тестами.

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_tournament_1(self):
        tst_n = 1
        test_1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[tst_n] = test_1.start()
        self.assertTrue(self.all_results[tst_n][len(self.all_results[tst_n])] == self.runner_3)

    def test_tournament_2(self):
        tst_n = 2
        test_2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[tst_n] = test_2.start()
        self.assertTrue(self.all_results[tst_n][len(self.all_results[tst_n])] == self.runner_3)

    def test_tournament_3(self):
        tst_n = 3
        test_3 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        self.all_results[tst_n] = test_3.start()
        self.assertTrue(self.all_results[tst_n][len(self.all_results[tst_n])] == self.runner_3)

        # Дополнительный тест, выявляющий ошибку в логике. Бегун 'Андрей' должен быть вторым.
        # self.assertTrue(self.all_results[tst_n][len(self.all_results[tst_n])-1] == self.runner_2)

    # Дополнительные тесты.

    # def test_tournament_4(self):
    #     tst_4 = 4
    #     tst_5 = 5
    #     tst_6 = 6
    #     test_4 = Tournament(90, self.runner_1, self.runner_3)
    #     test_5 = Tournament(90, self.runner_2, self.runner_3)
    #     test_6 = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
    #     self.all_results[tst_4] = test_4.start()
    #     self.all_results[tst_5] = test_5.start()
    #     self.all_results[tst_6] = test_6.start()
    #
    #     self.assertTrue(self.all_results[tst_4][len(self.all_results[tst_4])] == self.runner_3.name)
    #     self.assertTrue(self.all_results[tst_5][len(self.all_results[tst_5])] == self.runner_3.name)
    #     self.assertTrue(self.all_results[tst_6][len(self.all_results[tst_6])] == self.runner_3.name)



    @classmethod
    def tearDownClass(cls):
        all_results_new = {}
        for keys, values in cls.all_results.items():
            for k, v in values.items():
                all_results_new[k] = v.name
            print(all_results_new)


if __name__ == '__main__':
    unittest.main()
