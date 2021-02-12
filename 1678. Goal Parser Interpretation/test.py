import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input "G()(al)"
    def test_interpret_input1(self):
        self.assertEqual(sol.interpret("G()(al)"), "Goal")
    
    #Check for input "G()()()()(al)"
    def test_interpret_input2(self):
        self.assertEqual(sol.interpret("G()()()()(al)"), "Gooooal")

    #Check for input "(al)G(al)()()G"
    def test_interpret_input3(self):
        self.assertEqual(sol.interpret("(al)G(al)()()G"), "alGalooG")

if __name__ == '__main__':
    unittest.main()