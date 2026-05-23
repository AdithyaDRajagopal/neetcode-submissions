class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        processed = set()

        for i, num in enumerate(nums):
            if num in processed:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    triplets.append([num, nums[l], nums[r]])
                    left, right = nums[l], nums[r]
                    while l < r and nums[l] == left:
                        l += 1
                    while r > l and nums[r] == right:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

            processed.add(num)

        return triplets