n = int(input())
students = []
for i in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

students = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])