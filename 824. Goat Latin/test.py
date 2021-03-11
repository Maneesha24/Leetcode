import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 'I speak Goat Latin'
    def test_toGoatLatin_input1(self):
        self.assertEqual(sol.toGoatLatin('I speak Goat Latin'), 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa')
    
    #Check for input 'The quick brown fox jumped over the lazy dog'
    def test_toGoatLatin_input2(self):
        self.assertEqual(sol.toGoatLatin('The quick brown fox jumped over the lazy dog'), 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa')

    #Check for input 'Good morning'
    def test_toGoatLatin_input3(self):
        self.assertEqual(sol.toGoatLatin('Good morning'), 'oodGmaa orningmmaaa')

if __name__ == '__main__':
    unittest.main()