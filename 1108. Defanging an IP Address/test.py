import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input "1.1.1.1"
    def test_defangIPaddr_input1(self):
        self.assertEqual(sol.defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")
    
    #Check for input "255.100.50.0"
    def test_defangIPaddr_input2(self):
        self.assertEqual(sol.defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")

    #Check for input "20.21.123"
    def test_defangIPaddr_input3(self):
        self.assertEqual(sol.defangIPaddr("20.21.123"), "20[.]21[.]123")

if __name__ == '__main__':
    unittest.main()