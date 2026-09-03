class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, st, mid, end):
            temp = []
            i, j = st, mid + 1
            while i <= mid and j <= end:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= end:
                temp.append(nums[j])
                j += 1

            i = 0
            for idx in range(st, end + 1):
                nums[idx] = temp[i]
                i += 1


        def mergeSort(nums, st, end):
            if st < end:
                mid = st + (end - st)//2
                mergeSort(nums, st, mid)
                mergeSort(nums, mid + 1, end)
                merge(nums, st, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return nums