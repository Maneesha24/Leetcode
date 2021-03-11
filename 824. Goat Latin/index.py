class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        result = ''
        words = S.split(' ')
        i = 0
        while(i < len(words)):
            if words[i][0].lower() in vowels:
                result += words[i] + 'ma' + self.appendA(i + 1, len(words))
            else:
                result += words[i][1:] + words[i][0] + 'ma' + self.appendA(i + 1, len(words))
            i += 1

        return result

    def appendA(self, index, length):
        str = ''
        i = 0
        while(i < index):
            if i == index - 1:
                str += 'a'
            else:
                str += 'a'  
            i += 1
        return str if index == length else str + ' '

sol = Solution()
print(sol.toGoatLatin('I speak Goat Latin'))