import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3,3]
    def test_repeatedNTimes_input1(self):
        self.assertEqual(sol.repeatedNTimes([1,2,3,3]), 3)
    
    #Check for input [2,1,2,5,3,2]
    def test_repeatedNTimes_input2(self):
        self.assertEqual(sol.repeatedNTimes([2,1,2,5,3,2]), 2)

    #Check for input [5,1,5,2,5,3,5,4]
    def test_repeatedNTimes_input3(self):
        self.assertEqual(sol.repeatedNTimes([5,1,5,2,5,3,5,4]), 5)

if __name__ == '__main__':
    unittest.main()