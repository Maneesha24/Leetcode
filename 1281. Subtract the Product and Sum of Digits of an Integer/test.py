import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 234
    def test_subtractProductAndSum_input1(self):
        self.assertEqual(sol.subtractProductAndSum(234), 15)
    
    #Check for input 4421
    def test_subtractProductAndSum_input2(self):
        self.assertEqual(sol.subtractProductAndSum(4421), 21)

    #Check for input 12532
    def test_subtractProductAndSum_input3(self):
        self.assertEqual(sol.subtractProductAndSum(12532), 47)

if __name__ == '__main__':
    unittest.main()