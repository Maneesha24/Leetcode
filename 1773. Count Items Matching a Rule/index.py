class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        attributes = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        count = 0
        for val in items:
            if val[attributes[ruleKey]] == ruleValue:
                count += 1
        return count

sol = Solution()
print(sol.countMatches([
    ["phone","blue","pixel"],
    ["computer","silver","lenovo"],
    ["phone","gold","iphone"]], 'color', 'silver'))