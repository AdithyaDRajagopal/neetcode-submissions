class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)

        pairs = 0
        for key in count:
            n = count[key]
            if n > 1:
                pairs += (n * (n-1))//2
        
        return pairs