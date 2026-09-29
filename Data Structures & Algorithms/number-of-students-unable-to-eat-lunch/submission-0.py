class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        skips = 0
        while len(students) > 0 and skips < len(students):
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                skips = 0
            else:
                students = students[1:] + [students[0]]
                skips += 1
        
        return len(students)

        