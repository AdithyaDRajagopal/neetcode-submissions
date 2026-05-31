class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, l, r):
            nums[l], nums[r] = nums[r], nums[l]

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            val = nums[mid]
            if val == 0:
                swap(nums, low, mid)
                low += 1
                mid += 1
            elif val == 1:
                mid += 1
            else:
                swap(nums, mid, high)
                high -= 1
