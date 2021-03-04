import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([2,3,4,7,11], 5))
    def test_findKthPositive_input1(self):
        self.assertEqual(sol.findKthPositive([2,3,4,7,11], 5), 9)
    
    #Check for input ([1,2,3,4], 2))
    def test_findKthPositive_input2(self):
        self.assertEqual(sol.findKthPositive([1,2,3,4], 2), 6)

    #Check for input ([1,2,8,10], 3))
    def test_findKthPositive_input3(self):
        self.assertEqual(sol.findKthPositive([1,2,8,10], 3), 5)

if __name__ == '__main__':
    unittest.main()