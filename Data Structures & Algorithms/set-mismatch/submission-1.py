class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalSum = 0
        expectedSum = n * (n+1) // 2
        duplicate = -1

        s = set()
        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)
            totalSum += num

        missing = expectedSum - totalSum + duplicate
        return [duplicate, missing]