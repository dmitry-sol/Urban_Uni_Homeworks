import unittest
import module_12_1_updated
import module_12_2_updated

new_tournament_test = unittest.TestSuite()
new_tournament_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1_updated.RunnerTest))
new_tournament_test.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_updated.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(new_tournament_test)