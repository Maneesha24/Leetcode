import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3,2]
    def test_sumOfUnique_input1(self):
        self.assertEqual(sol.sumOfUnique([1,2,3,2]), 4)
    
    #Check for input [1,1,1,1,1]
    def test_sumOfUnique_input2(self):
        self.assertEqual(sol.sumOfUnique([1,1,1,1,1]), 0)

    #Check for input [1,2,3,4,5]
    def test_sumOfUnique_input3(self):
        self.assertEqual(sol.sumOfUnique([1,2,3,4,5]), 15)

if __name__ == '__main__':
    unittest.main()