class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        res = []
        for num in arr2:
            res += [num] * count.pop(num)
        
        for num in sorted(count):
            res += [num] * count[num]

        return res