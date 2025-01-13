import unittest
import module_12_1
import module_12_2

tsuite = unittest.TestSuite()
tsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
tsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
trunner = unittest.TextTestRunner(verbosity=2)
trunner.run(tsuite)

