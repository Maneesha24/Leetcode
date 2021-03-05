import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [10,2,5,3]
    def test_checkIfExist_input1(self):
        self.assertEqual(sol.checkIfExist([10,2,5,3]), True)
    
    #Check for input [7,1,14,11]
    def test_checkIfExist_input2(self):
        self.assertEqual(sol.checkIfExist([7,1,14,11]), True)

    #Check for input [3,1,7,11]
    def test_checkIfExist_input3(self):
        self.assertEqual(sol.checkIfExist([3,1,7,11]), False)

    #Check for input [-2,0,10,-19,4,6,-8]
    def test_checkIfExist_input4(self):
        self.assertEqual(sol.checkIfExist([-2,0,10,-19,4,6,-8]), False)

if __name__ == '__main__':
    unittest.main()