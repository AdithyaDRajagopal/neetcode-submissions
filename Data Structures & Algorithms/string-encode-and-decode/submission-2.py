class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + delimiter + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        delimiter = '#'
        decoded = []

        i = 0
        while i < len(s):
            l = 0
            while s[i] != delimiter:
                if s[i].isdigit():
                    l = l * 10 + int(s[i])
                i += 1
            
            i += 1
            word = s[i:i+l]
            decoded.append(word)
            i += l

        return decoded