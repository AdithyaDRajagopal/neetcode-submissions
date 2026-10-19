class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        res = len(students)

        for s in sandwiches:
            if count[s] > 0:
                res -= 1
                count[s] -= 1
            else:
                break
        
        return res
