import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 27
    def test_isPowerOfThree_input1(self):
        self.assertEqual(sol.isPowerOfThree(27), True)
    
    #Check for input 0
    def test_isPowerOfThree_input2(self):
        self.assertEqual(sol.isPowerOfThree(0), False)

    #Check for input 9
    def test_isPowerOfThree_input3(self):
        self.assertEqual(sol.isPowerOfThree(9), True)

    #Check for input 45
    def test_isPowerOfThree_input4(self):
        self.assertEqual(sol.isPowerOfThree(45), False)

if __name__ == '__main__':
    unittest.main()