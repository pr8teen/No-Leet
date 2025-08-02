class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        temp.append(nums[0])
        for i in range(1,len(nums)):
            x = nums[i] + temp[i-1]
            temp.append(x)
        return temp