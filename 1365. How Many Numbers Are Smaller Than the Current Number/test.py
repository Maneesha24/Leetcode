import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [8,1,2,2,3]
    def test_smallerNumbersThanCurrent_input1(self):
        self.assertEqual(sol.smallerNumbersThanCurrent([8,1,2,2,3]), [4, 0, 1, 1, 3])
    
    #Check for input [6,5,4,8]
    def test_smallerNumbersThanCurrent_input2(self):
        self.assertEqual(sol.smallerNumbersThanCurrent([6,5,4,8]), [2, 1, 0, 3])

    #Check for input [7,7,7,7]
    def test_smallerNumbersThanCurrent_input3(self):
        self.assertEqual(sol.smallerNumbersThanCurrent([7,7,7,7]), [0,0,0,0])

if __name__ == '__main__':
    unittest.main()