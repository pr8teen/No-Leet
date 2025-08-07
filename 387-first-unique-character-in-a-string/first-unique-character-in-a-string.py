
class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = Counter(s)
        for i in range(len(s)):
            if f[s[i]] == 1:
                return i
        return -1
