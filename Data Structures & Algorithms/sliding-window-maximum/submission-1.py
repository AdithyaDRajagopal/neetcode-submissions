class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        l = 0

        for r in range(len(nums)):
            while len(queue) and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)
            window = r - l + 1

            if window == k:
                res.append(nums[queue[0]])
                if queue[0] == l:
                    queue.popleft()
                l += 1
        
        return res