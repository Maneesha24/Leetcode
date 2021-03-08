import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 5
    def test_findComplement_input1(self):
        self.assertEqual(sol.findComplement(5), 2)
    
    #Check for input 1
    def test_findComplement_input2(self):
        self.assertEqual(sol.findComplement(1), 0)

    #Check for input 9
    def test_findComplement_input3(self):
        self.assertEqual(sol.findComplement(9), 6)

if __name__ == '__main__':
    unittest.main()