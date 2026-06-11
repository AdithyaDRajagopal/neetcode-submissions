class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, st, end):
            while st < end:
                nums[st], nums[end] = nums[end], nums[st]
                st += 1
                end -= 1
            print(nums)
            return nums

        n = len(nums)
        k = k%n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)