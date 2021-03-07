import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [12,345,2,6,7896]
    def test_findNumbers_input1(self):
        self.assertEqual(sol.findNumbers([12,345,2,6,7896]), 2)
    
    #Check for input [555,901,482,1771]
    def test_findNumbers_input2(self):
        self.assertEqual(sol.findNumbers([555,901,482,1771]), 1)

    #Check for input [1,1,1,261,6,13,3,3,10]
    def test_findNumbers_input3(self):
        self.assertEqual(sol.findNumbers([1,1,1,261,6,13,3,3,10]), 2)

if __name__ == '__main__':
    unittest.main()