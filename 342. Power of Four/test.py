import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 16
    def test_isPowerOfFour_input1(self):
        self.assertEqual(sol.isPowerOfFour(16), True)
    
    #Check for input 5
    def test_isPowerOfFour_input2(self):
        self.assertEqual(sol.isPowerOfFour(5), False)

    #Check for input 1
    def test_isPowerOfFour_input3(self):
        self.assertEqual(sol.isPowerOfFour(1), True)

if __name__ == '__main__':
    unittest.main()