import math

# looked at hints


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def tToF(piles, k, h):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h  # if false means that means the k is too slow

        low, high = 1, max(piles)
        # binary search to find the minimum possible k
        while low < high:
            mid = (low + high) // 2
            if tToF(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        return low
