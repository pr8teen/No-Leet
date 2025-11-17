class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi = 0
        x = {}
        for i in range(len(nums)):
            x[nums[i]]=x.get(nums[i],0) +1
        c=0
        for j in x:
            if maxi<x[j]:
                maxi=x[j]
                c=j 
        return c