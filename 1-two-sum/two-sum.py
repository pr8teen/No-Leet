class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mera approach:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i]+ nums[j] != target:
        #             continue
        #         else:
        #             return [i,j]

        # optimal approach
        n = len(nums)
        dict1 ={}
        for i in range(n):
            rem = target - nums[i]
            if rem in dict1:
                return[dict1[rem],i]
            else:
                dict1[nums[i]] = i