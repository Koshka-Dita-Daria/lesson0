
import unittest
from Runner_Tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.r1 = Runner("Усэйн", 10)
        self.r2 = Runner("Андрей", 9)
        self.r3 = Runner("Ник", 3)
    @classmethod
    def setUpClass(cls):
        cls.all_result = []
    @classmethod
    def tearDownClass(cls):
        for i, el in enumerate(cls.all_result):
            print(f"{i}: {el}")
    def runners1(self):
        l1 = Tournament(90, self.r1, self.r3)
        res1 = l1.start()
        TournamentTest.all_result.append(res1)
        self.assertTrue(res1[2] == "Ник")
    def runners2(self):
        l2 = Tournament(90, self.r2, self.r3)
        res2 = l2.start()
        TournamentTest.all_result.append(res2)
        self.assertTrue(res2[2] == "Ник")
    def runners3(self):
        l3 = Tournament(90, self.r1, self.r2, self.r3)
        res3 = l3.start()
        TournamentTest.all_result.append(res3)
        self.assertTrue(res3[3] == "Ник")