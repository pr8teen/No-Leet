class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target in nums:
                return nums.index(target)
            elif target not in nums:
                if target<nums[i]:
                    return i
        return len(nums)
