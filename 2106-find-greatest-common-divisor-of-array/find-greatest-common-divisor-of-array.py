class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        x = []
        for i in range(1,mx+1):
            if mx % i == 0 and mn % i ==0:
                x.append(i)
        return max(x)
        