class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set([i for i in range(1, len(nums) + 1)])
        
        for num in nums:
            if num in s:
                s.remove(num)

        return list(s)