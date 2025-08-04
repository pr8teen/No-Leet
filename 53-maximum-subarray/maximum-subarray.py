class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_s = 0
        max_s = nums[0]

        for i in range(len(nums)):
            curr_s += nums[i]
            if curr_s > max_s:
                max_s = curr_s
            if curr_s<0:
                curr_s = 0
        return max_s