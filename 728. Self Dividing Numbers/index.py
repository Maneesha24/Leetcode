class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result_arr = []
        for num in range(left, right + 1):
            num_val = str(num)
            i = 0
            count = 0
            while(i < len(num_val)):
                if num_val[i] != '0' and num%int(num_val[i]) == 0:
                    count += 1
                i += 1
            if count == len(num_val):
                result_arr.append(num)
        return result_arr
                
sol = Solution()
print(sol.selfDividingNumbers(1, 22))