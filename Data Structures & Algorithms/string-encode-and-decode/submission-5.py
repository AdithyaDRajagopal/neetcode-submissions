class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + delimiter + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        delimiter = '#'

        print(s)
        while idx < len(s):
            length = 0
            while s[idx] != delimiter:
                length = length * 10 + int(s[idx])
                idx += 1
            
            idx += 1
            string = ''
            for i in range(idx, idx + length):
                string += s[i]
            decoded.append(string)
            idx += length
        return decoded