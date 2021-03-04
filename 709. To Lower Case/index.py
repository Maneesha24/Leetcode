class Solution:
    def toLowerCase(self, str: str) -> str:
        result_str = ''
        for char in str:
            if ord(char) >=65 and ord(char) <= 90:
                 result_str += chr(ord(char) + 32)
            else:
                 result_str += char
        
        return result_str
        

sol = Solution()
print(sol.toLowerCase("Hello"))