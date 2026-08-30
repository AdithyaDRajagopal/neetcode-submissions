class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for f in freq:
            bucket[freq[f]].append(f)
        
        res = []
        for b in range(len(bucket) - 1, -1, -1):
            for i in bucket[b]:
                res.append(i)
            
            if len(res) == k:
                return res