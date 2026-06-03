from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = Counter(students)
        for i in sandwiches:
            if students.get(i, 0) > 0:
                sandwiches = sandwiches[1:]
                students[i] -= 1
            else: 
                return len(sandwiches)
        return 0
        