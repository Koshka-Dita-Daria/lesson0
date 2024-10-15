import unittest
import Tests_12_3

runRT = unittest.TestSuite()
runRT.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.TournamentTest))
runRT.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runRT)