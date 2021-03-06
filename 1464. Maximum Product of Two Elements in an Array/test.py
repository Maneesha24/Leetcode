import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [3,4,5,2]
    def test_maxProduct_input1(self):
        self.assertEqual(sol.maxProduct([3,4,5,2]), 12)
    
    #Check for input [1,5,4,5]
    def test_maxProduct_input2(self):
        self.assertEqual(sol.maxProduct([1,5,4,5]), 16)

    #Check for input [3,7]
    def test_maxProduct_input3(self):
        self.assertEqual(sol.maxProduct([3,7]), 12)

    #Check for input [1,1,1,1]
    def test_maxProduct_input4(self):
        self.assertEqual(sol.maxProduct([1,1,1,1]), 0)

if __name__ == '__main__':
    unittest.main()