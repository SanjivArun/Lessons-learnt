marks = {}

num_of_students = int(input("Please enter number of students: "))

for i in range(num_of_students):
    mark = int(input("Enter mark: "))
    marks.append(mark)

# sort marks
marks.sort()
print(marks)
