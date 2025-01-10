from unittest import TestCase
from HumanMoveTest.runner import Runner

class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('runner_test_1')
        for epoch in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('runner_test_2')
        for epoch in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner('runner_test_1')
        runner2 = Runner('runner_test_2')
        for epoch in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

