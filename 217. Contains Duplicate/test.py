import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input [1,2,3,1]
    def test_containsDuplicate_input1(self):
        self.assertEqual(sol.containsDuplicate([1,2,3,1]), True)
    
    #Check for input [1,2,3,4]
    def test_containsDuplicate_input2(self):
        self.assertEqual(sol.containsDuplicate([1,2,3,4]), False)

    #Check for input [1,1,1,3,3,4,3,2,4,2]
    def test_containsDuplicate_input3(self):
        self.assertEqual(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()