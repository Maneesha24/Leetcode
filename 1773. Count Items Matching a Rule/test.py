import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input ([["phone","blue","pixel"], ["computer","silver","lenovo"],["phone","gold","iphone"]], 'color', 'silver')
    def test_countMatches_input1(self):
        self.assertEqual(sol.countMatches([
    ["phone","blue","pixel"],
    ["computer","silver","lenovo"],
    ["phone","gold","iphone"]], 'color', 'silver'), 1)
    
    #Check for input ([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], 'type', 'phone')
    def test_countMatches_input2(self):
        self.assertEqual(sol.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], 'type', 'phone'), 2)

    #Check for input ([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], 'name', 'iphone')
    def test_countMatches_input3(self):
        self.assertEqual(sol.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], 'name', 'iphone'), 1)

if __name__ == '__main__':
    unittest.main()