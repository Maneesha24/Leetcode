import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input "UD"
    def test_judgeCircle_input1(self):
        self.assertEqual(sol.judgeCircle("UD"), True)
    
    #Check for input "RRDD"
    def test_judgeCircle_input2(self):
        self.assertEqual(sol.judgeCircle("RRDD"), False)

    #Check for input "LDRRLRUULR"
    def test_judgeCircle_input3(self):
        self.assertEqual(sol.judgeCircle("LDRRLRUULR"), False)

if __name__ == '__main__':
    unittest.main()