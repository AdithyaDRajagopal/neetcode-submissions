class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        delimiter = '#'
        for s in strs:
            encoded += str(len(s)) + delimiter + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        delimiter = '#'
        decoded = []

        i = 0
        while i < len(s):
            l = 0
            
            while s[i] != '#':
                l = 10 * l + int(s[i])
                i += 1
            
            i += 1
            decoded.append(s[i:i+l])
            i += l

        return decoded