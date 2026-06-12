class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(piles, h, maxAllowed):
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/maxAllowed)
            return totalHours <= h

        n = len(piles)
        st, end = 1, max(piles)
        res = end

        while st <= end:
            mid = st + (end - st)//2

            if isValid(piles, h, mid):
                res = mid
                end = mid - 1
            else:
                st = mid + 1
        
        return res