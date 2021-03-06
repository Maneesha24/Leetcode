class Solution:
    def arrayStringsAreEqual(self, word1, word2):

        string1 = self.getStringVal(word1)
        string2 = self.getStringVal(word2)

        return string1 == string2
    
    def getStringVal(self, arr):
        stringVal = ''
        
        for char in  arr:
            stringVal += char
        
        return stringVal

sol = Solution()
print(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))