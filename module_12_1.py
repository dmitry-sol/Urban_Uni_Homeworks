import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):

    def test_walk(self):
        test_walker = Runner('Yuriy')
        for i in range(10):
            test_walker.walk()
        self.assertEqual(test_walker.distance, 50)

    def test_run(self):
        test_runner = Runner('Semion')
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_walker = Runner('Dasha')
        test_runner = Runner('Yana')
        for i in range(10):
            test_walker.walk()
            test_runner.run()
        self.assertNotEqual(test_walker.distance, test_runner.distance)


if __name__ == '__main__':
    unittest.main()
