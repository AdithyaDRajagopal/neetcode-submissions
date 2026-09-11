class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = { 0: 1 }
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            if prefixSum - k in hashMap:
                count += hashMap[prefixSum - k]
            hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1

        return count