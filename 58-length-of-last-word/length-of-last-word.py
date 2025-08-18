class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.strip()
        x = list(map(str,y.split(" ")))
        n= len(x)
        return len(x[n-1])