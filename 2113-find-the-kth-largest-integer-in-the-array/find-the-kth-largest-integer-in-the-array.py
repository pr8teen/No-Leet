class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        unique_nums = list(map(int,set(nums)))
        norm = list(map(int,nums))
        if len(unique_nums) < 2:
            return str(unique_nums[0])
        norm.sort()
        return str(norm[-k])