class Solution:
    def isUgly(self, num: int) -> bool:
        while(num > 1):
            if num%2 == 0:
                num = num//2
            elif num%3 == 0:
                num = num//3
            elif num%5 == 0:
                num = num//5
            else:
                return False
        
        return True if num == 1 else False

sol = Solution()
print(sol.isUgly(6))