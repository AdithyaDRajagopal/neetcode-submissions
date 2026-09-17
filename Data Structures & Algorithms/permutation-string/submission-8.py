class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = Counter(s2[:len(s1)])
        freq = Counter(s1)

        for i in range(len(s1), len(s2)):
            if window == freq:
                return True
            
            st = i - len(s1)
            window[s2[st]] -= 1
            if not window[s2[st]]:
                del window[s2[st]]
            window[s2[i]] = window.get(s2[i], 0) + 1

        return window == freq        
