class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums) - 1

        while st <= end:
            mid = st + (end - st)//2
            if target == nums[mid]:
                return mid
            
            if nums[st] <= nums[mid]:
                if target >= nums[st] and target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1

        return -1