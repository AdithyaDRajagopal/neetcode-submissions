class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        freq = {}
        for word in words:
            for letter in word:
                freq[letter] = freq.get(letter, 0) + 1
        
        for key in freq:
            if freq[key] % n != 0:
                return False
        
        return True