class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = [(h, n) for h, n in zip(heights, names)]
        pair.sort(reverse = True)
        
        return [name for height, name in pair]