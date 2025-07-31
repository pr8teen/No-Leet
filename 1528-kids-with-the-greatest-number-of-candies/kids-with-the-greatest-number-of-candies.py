class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        bulla = []
        for i in candies:
            extra = i+extraCandies
            if maxCandies <= extra:
                bulla.append(True)
            else:
                bulla.append(False)
        return bulla
        