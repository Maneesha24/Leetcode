class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return self.getVowelCount(s[: round(len(s)/2)]) == self.getVowelCount(s[round(len(s)/2): ])

    def getVowelCount(self, str):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

        result = 0
        for char in str:
            if char in vowels: 
                result += 1
        
        return result

                
sol = Solution()
print(sol.halvesAreAlike('book'))