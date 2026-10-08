class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        cnt = 0

        for val in arr:
            if count[val] == 1:
                cnt += 1
            
            if cnt == k:
                return val
        
        return ""