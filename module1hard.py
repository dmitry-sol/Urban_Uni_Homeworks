# module1hard

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

count = len(grades)
average_grade = []

for i in range(count):
    average_grade.append(round(sum(grades[i]) / len(grades[i]),2))

students = list(students)
students.sort()

average_grade_dict = dict(zip(students, average_grade))
print('Average grade of students:', average_grade_dict)
