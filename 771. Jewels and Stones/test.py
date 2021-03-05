import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ("aA", "aAAbbbb")
    def test_numJewelsInStones_input1(self):
        self.assertEqual(sol.numJewelsInStones("aA", "aAAbbbb"), 3)
    
    #Check for input ("z", "ZZ")
    def test_numJewelsInStones_input2(self):
        self.assertEqual(sol.numJewelsInStones("z", "ZZ"), 0)

    #Check for input ("zmK", "ZML")
    def test_numJewelsInStones_input3(self):
        self.assertEqual(sol.numJewelsInStones("zmK", "ZML"), 0)

if __name__ == '__main__':
    unittest.main()