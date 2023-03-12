marks = []

# User enters numbers
print("Find the MEDIAN!")  # OR len(marks)
num_count = int(input("Enter number of numbers: "))

for m in range(0, num_count):
    num = int(input("Enter num: "))
    marks.append(num)

# sort doesn't work properly
marks.sort()
print(marks)

# Find Median Hold
# % gives reminder in division

middle_index = int(num_count / 2)
print(middle_index)
if num_count % 2 == 0:
    median = (marks[middle_index] + marks[middle_index - 1]) / 2
    print(f"median of {marks} is {median}")

else:
    print("median is", marks[middle_index])
