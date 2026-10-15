class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0

        for word in words:
            consistent = True
            for letter in word:
                if letter not in allowed:
                    consistent = False
                    break
            
            if consistent:
                total += 1
        
        return total