class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = [0] * (len(words) + 1)

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count[i+1] += 1
            
            count[i+1] += count[i]
        
        res = []
        print(count)
        for q in queries:
            st, end = q[0], q[1]
            cnt = count[end+1] - count[st]
            res.append(cnt)

        return res
