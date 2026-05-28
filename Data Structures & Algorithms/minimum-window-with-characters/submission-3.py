class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        minWindow = float("infinity")
        count, window = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        have, need = 0, len(count)
        l = 0
        res = (-1, -1)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count and count[c] == window[c]:
                have += 1
            
            while have == need:
                windowLen = r - l + 1
                if windowLen < minWindow:
                    res = (l, r)
                    minWindow = windowLen
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if minWindow != float("infinity") else ''