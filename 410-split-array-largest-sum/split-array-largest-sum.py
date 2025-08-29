class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_feasible(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
            return True

        low, high = max(nums), sum(nums)
        minimized_largest_sum = high
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                minimized_largest_sum = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return minimized_largest_sum