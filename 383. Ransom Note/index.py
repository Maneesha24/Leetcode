class Solution:
    def canConstruct(self, ransomNote, magazine):
        charObj = {}

        for char in  magazine:
            if char in charObj:
                charObj[char] += 1
            else:
                charObj[char] = 1

        for char in ransomNote:
            if char not in charObj or charObj[char] == 0:
                return False
            else:
                charObj[char] -= 1
        
        return True

sol = Solution()
print(sol.canConstruct('a', 'b'))