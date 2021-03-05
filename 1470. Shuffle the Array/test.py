import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([2,5,1,3,4,7], 3)
    def test_shuffle_input1(self):
        self.assertEqual(sol.shuffle([2,5,1,3,4,7], 3), [2, 3, 5, 4, 1, 7])
    
    #Check for input ([1,2,3,4,4,3,2,1], 4)
    def test_shuffle_input2(self):
        self.assertEqual(sol.shuffle([1,2,3,4,4,3,2,1], 4), [1, 4, 2, 3, 3, 2, 4, 1])

    #Check for input ([1,1,2,2], 2)
    def test_shuffle_input3(self):
        self.assertEqual(sol.shuffle([1,1,2,2], 2), [1, 2, 1, 2])

if __name__ == '__main__':
    unittest.main()