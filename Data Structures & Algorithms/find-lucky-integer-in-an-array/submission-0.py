class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = -1

        for key in count:
            if key == count[key] and key > lucky:
                lucky = key

        return lucky