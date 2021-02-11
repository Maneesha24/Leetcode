import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3,4]
    def test_runningSum_input1(self):
        self.assertEqual(sol.runningSum([1,2,3,4]), [1,3,6,10])
    
    #Check for input [1,1,1,1,1]
    def test_runningSum_input2(self):
        self.assertEqual(sol.runningSum([1,1,1,1,1]), [1,2,3,4,5])

    #Check for input [3,1,2,10,1]
    def test_runningSum_input3(self):
        self.assertEqual(sol.runningSum([3,1,2,10,1]), [3,4,6,16,17])

if __name__ == '__main__':
    unittest.main()