class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp_even = []
        temp_odd = []
        nums.sort()
        for i in range (0,n):
            if nums[i] % 2 == 0:
                temp_even.append(nums[i])
            else:
                temp_odd.append(nums[i])
        temp_even.extend(temp_odd)
        return temp_even
            