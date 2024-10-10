import unittest
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

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.name = "1"
        Runner(self.name)
        for i in range(10):
            self.distance += Runner(1).walk()
        self.assertEqual(self.distance, 50)
    def test_run(self):
        self.name = Runner(2)
        for i in range(10):
            self.distance += self.run()
        self.assertEqual(self.distance, 100)
    def test_challenge(self):
        self.name = Runner(3)
        for i in range(10):
            self.distance = self.name.walk()
        self.name1 = Runner(4)
        for i in range(10):
            self.distance = self.name1.run()
        self.assertEqual(self.name, self.name1)
