import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([2,3,5,1,3], 3)
    def test_kidsWithCandies_input1(self):
        self.assertEqual(sol.kidsWithCandies([2,3,5,1,3], 3), [True, True, True, False, True])
    
    #Check for input ([4,2,1,1,2], 1)
    def test_kidsWithCandies_input2(self):
        self.assertEqual(sol.kidsWithCandies([4,2,1,1,2], 1), [True, False, False, False, False])

    #Check for input ([12,1,12], 10)
    def test_kidsWithCandies_input3(self):
        self.assertEqual(sol.kidsWithCandies([12,1,12], 10), [True, False, True])

if __name__ == '__main__':
    unittest.main()