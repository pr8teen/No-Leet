class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n1 = len(nums)
        n2 = len(nums)+1
        return sum(range(n2)) - sum(nums)