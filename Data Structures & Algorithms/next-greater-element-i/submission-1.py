class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if not stack:
                hashMap[nums2[i]] = -1
            else:
                hashMap[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        
        res = []
        for num in nums1:
            res.append(hashMap[num])
        return res