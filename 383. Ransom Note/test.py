import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ('a', 'b')
    def test_canConstruct_input1(self):
        self.assertEqual(sol.canConstruct('a', 'b'), False)
    
    #Check for input ('aa', 'ab')
    def test_canConstruct_input2(self):
        self.assertEqual(sol.canConstruct('aa', 'ab'), False)

    #Check for input ('aa', 'aab')
    def test_canConstruct_input3(self):
        self.assertEqual(sol.canConstruct('aa', 'aab'), True)

if __name__ == '__main__':
    unittest.main()