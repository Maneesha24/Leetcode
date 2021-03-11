import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,2,6,6,6,6,7,10]
    def test_findSpecialInteger_input1(self):
        self.assertEqual(sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]), 6)
    
    #Check for input [9,9,3,2,2,2,6,10]
    def test_findSpecialInteger_input2(self):
        self.assertEqual(sol.findSpecialInteger([9,9,3,2,2,2,6,10]), 2)

    #Check for input [1,1,1,6,6,3,3,3,10]
    def test_findSpecialInteger_input3(self):
        self.assertEqual(sol.findSpecialInteger([1,1,1,6,6,3,3,3,10]), 1)

if __name__ == '__main__':
    unittest.main()