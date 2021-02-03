class Solution:
    def numberOfSteps (self, num: int) -> int:
        step_count = 0
        while(num > 0):
            #Check if number is even and divide by 2
            if num%2 == 0:
                num = num//2
            #Check if number is odd and subtract by 1
            else:
                num = num - 1
            step_count += 1
        return step_count

sol = Solution()
print(sol.numberOfSteps(14))