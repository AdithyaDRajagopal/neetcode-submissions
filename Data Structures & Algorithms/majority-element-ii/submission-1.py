class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        res = []

        for i, count in freq.items():
            if count > n/3:
                res.append(i)

        return res