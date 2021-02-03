import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 14
    def test_numberOfSteps_input1(self):
        self.assertEqual(sol.numberOfSteps(14), 6)
    
    #Check for input 8
    def test_numberOfSteps_input2(self):
        self.assertEqual(sol.numberOfSteps(8), 4)

    #Check for input 123
    def test_numberOfSteps_input3(self):
        self.assertEqual(sol.numberOfSteps(123), 12)

if __name__ == '__main__':
    unittest.main()