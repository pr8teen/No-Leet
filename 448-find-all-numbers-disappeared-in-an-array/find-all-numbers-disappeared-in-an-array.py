class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(nums)
        x = []
        for i in range(1,len(nums)+1):
            if i not in n:
                x.append(i)
        return x