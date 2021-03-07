import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 6
    def test_isUgly_input1(self):
        self.assertEqual(sol.isUgly(6), True)
    
    #Check for input 8
    def test_isUgly_input2(self):
        self.assertEqual(sol.isUgly(8), True)

    #Check for input 14
    def test_isUgly_input3(self):
        self.assertEqual(sol.isUgly(14), False)

if __name__ == '__main__':
    unittest.main()