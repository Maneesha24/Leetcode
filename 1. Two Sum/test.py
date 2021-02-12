import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([2,7,11,15], 9))
    def test_twoSum_input1(self):
        self.assertEqual(sol.twoSum([2,7,11,15], 9), [0,1])
    
    #Check for input ([3,2,4], 6))
    def test_twoSum_input2(self):
        self.assertEqual(sol.twoSum([3,2,4], 6), [1,2])

    #Check for input ([3,3], 6))
    def test_twoSum_input3(self):
        self.assertEqual(sol.twoSum([3,3], 6), [0,1])

if __name__ == '__main__':
    unittest.main()