import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ("Hello")
    def test_toLowerCase_input1(self):
        self.assertEqual(sol.toLowerCase("Hello"), "hello")
    
    #Check for input ("here")
    def test_toLowerCase_input2(self):
        self.assertEqual(sol.toLowerCase("here"), "here")

    #Check for input ("LOVELY")
    def test_toLowerCase_input3(self):
        self.assertEqual(sol.toLowerCase("LOVELY"), "lovely")

if __name__ == '__main__':
    unittest.main()