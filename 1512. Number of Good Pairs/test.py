import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3,1,1,3]
    def test_numIdenticalPairs_input1(self):
        self.assertEqual(sol.numIdenticalPairs([1,2,3,1,1,3]), 4)
    
    #Check for input [1,1,1,1]
    def test_numIdenticalPairs_input2(self):
        self.assertEqual(sol.numIdenticalPairs([1,1,1,1]), 6)

    #Check for input [1,2,3]
    def test_numIdenticalPairs_input3(self):
        self.assertEqual(sol.numIdenticalPairs([1,2,3]), 0)

if __name__ == '__main__':
    unittest.main()