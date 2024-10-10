import unittest
from Runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = Runner('1')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)
    def test_run(self):
        r1 = Runner('2')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)
    def test_challenge(self):
        r1 = Runner('3')
        r2 = Runner('4')
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)
