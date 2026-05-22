class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)

        for f in freq:
            bucket[freq[f]].append(f)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if not len(bucket[i]):
                continue
            
            for b in bucket[i]:
                res.append(b)
            
            if len(res) == k:
                return res

        return res
