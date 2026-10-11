class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap, wordMap = {}, {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashMap:
                if words[i] in wordMap:
                    return False

                hashMap[pattern[i]] = words[i]
                wordMap[words[i]] = pattern[i]
                continue
            
            if hashMap[pattern[i]] != words[i]:
                return False
        
        return True
            