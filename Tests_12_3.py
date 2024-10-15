import sys
import unittest

import Runner_Tournament
from Runner_Tournament import Runner, Tournament
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = Runner('1')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r1 = Runner('2')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = Runner('3')
        r2 = Runner('4')
        for i in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)
class TournamentTest(unittest.TestCase):
    is_frozen = True


    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)
    @classmethod
    def setUpClass(cls):
        cls.all_result = []
    @classmethod
    def tearDownClass(cls):
        c = {}
        for i, el in enumerate(cls.all_result):
            for j in range(len(el)):
                k = Runner.__str__(el[j+1])
                c.update({j+1: k})
            print(c)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_runners1(self):
        l1 = Tournament(90, self.r1, self.r3)
        res1 = l1.start()
        TournamentTest.all_result.append(res1)
        self.assertTrue(res1[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_runners2(self):
        l2 = Tournament(90, self.r2, self.r3)
        res2 = l2.start()
        TournamentTest.all_result.append(res2)
        self.assertTrue(res2[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_runners3(self):
        l3 = Tournament(90, self.r1, self.r2, self.r3)
        res3 = l3.start()
        TournamentTest.all_result.append(res3)
        self.assertTrue(res3[3] == "Ник")