import unittest
from index import sol

class Testing(unittest.TestCase):

    #Check for input 15
    def test_fizzBuzz_input1(self):
        self.assertEqual(sol.fizzBuzz(15), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])
    
    #Check for input 9
    def test_fizzBuzz_input2(self):
        self.assertEqual(sol.fizzBuzz(9), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz'])

    #Check for input 25
    def test_fizzBuzz_input3(self):
        self.assertEqual(sol.fizzBuzz(25), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz'])

if __name__ == '__main__':
    unittest.main()