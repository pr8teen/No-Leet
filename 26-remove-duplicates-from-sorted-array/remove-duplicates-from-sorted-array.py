class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x= 0
        for i in range(1,len(nums)):
            if nums[i] != nums[x]:
                x+=1
                nums[x] = nums[i]
        y = x+1
        return y