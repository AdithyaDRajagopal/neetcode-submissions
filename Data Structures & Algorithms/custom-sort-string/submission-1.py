class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""
        for c in order:
            res += c * count[c]
            del count[c]
        
        for c in count:
            res += c * count[c]

        return ''.join(res)