n = int(input())
student = []
for i in range(n):
    input_data = input().split()
    student.append((input_data[0], int(input_data[1])))
print(student)
student = sorted(student, key=lambda array: array[1])
for student_name in student:
    print(student_name[0], end=" ")
