class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        res = strs[0]
        
        for s in strs[1:]:
            for i in range(len(res)):
                if s[i] != res[i]:
                    res = res[:i]
                    break

        return res