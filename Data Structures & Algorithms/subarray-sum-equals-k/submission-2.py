class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        hashMap = { 0: 1 }

        for num in nums:
            prefixSum += num
            diff = prefixSum - k
            if diff in hashMap:
                count += hashMap[diff]
            
            hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1

        return count