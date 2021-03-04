import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [3,1,2,4]
    def test_sortArrayByParity_input1(self):
        self.assertEqual(sol.sortArrayByParity([3,1,2,4]), [4, 2, 3, 1])
    
    #Check for input [5,3,2,1,6,2,7]
    def test_sortArrayByParity_input2(self):
        self.assertEqual(sol.sortArrayByParity([5,3,2,1,6,2,7]), [2, 6, 2, 5, 3, 1, 7])

    #Check for input [1,1,0,0,2,4,3]
    def test_sortArrayByParity_input3(self):
        self.assertEqual(sol.sortArrayByParity([1,1,0,0,2,4,3]), [4, 2, 0, 0, 1, 1, 3])

if __name__ == '__main__':
    unittest.main()