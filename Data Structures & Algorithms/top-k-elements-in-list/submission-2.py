class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        freq = Counter(nums)
        for f in freq:
            bucket[freq[f]].append(f)

        res = []

        for b in range(len(bucket)-1, -1, -1):
            if not len(bucket[b]):
                continue

            for num in bucket[b]:
                res.append(num)
                if len(res) == k:
                    return res
