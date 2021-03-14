import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([0,1,2,3,4], [0,1,2,2,1])
    def test_createTargetArray_input1(self):
        self.assertEqual(sol.createTargetArray([0,1,2,3,4], [0,1,2,2,1]), [0,4,1,3,2])
    
    #Check for input ([1,2,3,4,0], [0,1,2,3,0])
    def test_createTargetArray_input2(self):
        self.assertEqual(sol.createTargetArray([1,2,3,4,0], [0,1,2,3,0]), [0, 1, 2, 3, 4])

    #Check for input ([1], [0])
    def test_createTargetArray_input3(self):
        self.assertEqual(sol.createTargetArray([1], [0]), [1])

if __name__ == '__main__':
    unittest.main()