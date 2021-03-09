import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input (1, 22)
    def test_selfDividingNumbers_input1(self):
        self.assertEqual(sol.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
    
    #Check for input (1, 43)
    def test_selfDividingNumbers_input2(self):
        self.assertEqual(sol.selfDividingNumbers(1, 43), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36])

    #Check for input (7, 15)
    def test_selfDividingNumbers_input3(self):
        self.assertEqual(sol.selfDividingNumbers(7, 15), [7, 8, 9, 11, 12, 15])

if __name__ == '__main__':
    unittest.main()