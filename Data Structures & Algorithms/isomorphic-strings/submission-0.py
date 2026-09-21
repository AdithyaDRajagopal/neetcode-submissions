class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS, mapT = {}, {}
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = i
            
            if t[i] not in mapT:
                mapT[t[i]] = i
            
            if mapS[s[i]] != mapT[t[i]]:
                return False
        
        return True