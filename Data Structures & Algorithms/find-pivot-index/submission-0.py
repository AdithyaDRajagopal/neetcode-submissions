class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum, rightSum = [0] * n, [0] * n
        
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        if leftSum[0] == rightSum[0]:
            return 0

        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

            if leftSum[i] == rightSum[i]:
                return i
        
        return -1        
        