class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        count = Counter(magazine)

        for letter in note:
            if note[letter] > count.get(letter, 0):
                return False
            
        return True