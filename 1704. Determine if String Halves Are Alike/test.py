import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 'textbook'
    def test_halvesAreAlike_input1(self):
        self.assertEqual(sol.halvesAreAlike('textbook'), False)
    
    #Check for input 'MerryChristmas'
    def test_halvesAreAlike_input2(self):
        self.assertEqual(sol.halvesAreAlike('MerryChristmas'), False)

    #Check for input 'AbCdEfGh'
    def test_halvesAreAlike_input3(self):
        self.assertEqual(sol.halvesAreAlike('AbCdEfGh'), True)

    #Check for input 'ebeilA'
    def test_halvesAreAlike_input4(self):
        self.assertEqual(sol.halvesAreAlike('ebeilA'), True)

if __name__ == '__main__':
    unittest.main()