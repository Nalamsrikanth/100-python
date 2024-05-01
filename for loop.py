student_height = input().split()
print(student_height)
num_stu = len(student_height)
print(num_stu)
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_height = 0
for height in student_height:
    total_height += height
avg_height = total_height / len(student_height)

print(f"average height of class is {int(avg_height)}")