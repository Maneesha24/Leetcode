class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        i = 0
        count = 0
        str1length = len(jewels)
        str2length = len(stones)
        while(i < str1length):
            j = 0
            while(j < str2length):
                if jewels[i] == stones[j]:
                    count += 1
                j += 1
            i += 1
        return count


sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))