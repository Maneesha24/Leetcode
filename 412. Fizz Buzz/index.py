class Solution:
    def fizzBuzz(self, n: int):
        result_arr = []

        for val in range(1, n + 1):
            if val%3 == 0 and val%5 == 0:
                result_arr.append('FizzBuzz')
            elif val%3 == 0:
                result_arr.append('Fizz')
            elif val%5 == 0:
                result_arr.append('Buzz')
            else:
                result_arr.append(f'{val}')
        
        return result_arr

sol = Solution()
print(sol.fizzBuzz(15))