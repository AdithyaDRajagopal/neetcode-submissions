class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats = 0

        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats += 1
        
        return boats