class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words[1:]:
            curr = Counter(word)

            for key in count:
                if key in curr:
                    count[key] = min(count[key], curr[key])
                else:
                    count[key] = 0
        
        res = []
        for key in count:
            if count[key] > 0:
                res.extend(key * count[key])

        return res