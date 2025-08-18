class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        for ele in nums1:
            if ele in nums2:
                r.append(ele)
                nums2.remove(ele)
        return r