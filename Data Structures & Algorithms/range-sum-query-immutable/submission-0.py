class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sumArray = [0] * (n + 1)
        for i in range(1, n + 1):
            self.sumArray[i] = self.sumArray[i-1] + nums[i-1]
        print(self.sumArray)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumArray[right + 1] - self.sumArray[left]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)