class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        length = 0
        for word in words:
            wordCount = Counter(word)

            good = True
            for letter in wordCount:
                if wordCount[letter] > count.get(letter, 0):
                    good = False
                    break
            
            if good:
                length += len(word)
        
        return length