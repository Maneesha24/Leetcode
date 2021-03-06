import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input (["ab", "c"], ["a", "bc"])
    def test_arrayStringsAreEqual_input1(self):
        self.assertEqual(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), True)
    
    #Check for input (["a", "cb"], ["ab", "c"])
    def test_arrayStringsAreEqual_input2(self):
        self.assertEqual(sol.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), False)

    #Check for input (["abc", "d", "defg"], ["abcddefg"])
    def test_arrayStringsAreEqual_input3(self):
        self.assertEqual(sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), True)

if __name__ == '__main__':
    unittest.main()