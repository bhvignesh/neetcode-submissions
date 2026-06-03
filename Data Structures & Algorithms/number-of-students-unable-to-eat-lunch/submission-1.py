from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = Counter(students)
        n_sandwiches = len(sandwiches)
        for i in sandwiches:
            if students.get(i, 0) > 0:
                n_sandwiches -=1
                students[i] -= 1
            else: 
                return n_sandwiches
        return 0
        