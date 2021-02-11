import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3],[3,2,1]]
    def test_maximumWealth_input1(self):
        self.assertEqual(sol.maximumWealth([[1,2,3],[3,2,1]]), 6)
    
    #Check for input [[1,5],[7,3],[3,5]]
    def test_maximumWealth_input2(self):
        self.assertEqual(sol.maximumWealth([[1,5],[7,3],[3,5]]), 10)

    #Check for input [[2,8,7],[7,1,3],[1,9,5]]
    def test_maximumWealth_input3(self):
        self.assertEqual(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]), 17)

if __name__ == '__main__':
    unittest.main()