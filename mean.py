marks = []

# User enters numbers
print("Find the MEAN!")  # OR len(marks)
num_count = int(input("Enter number of numbers you would like to import: "))

for m in range(0, num_count):
    num = int(input("Enter num: "))
    marks.append(num)

# Find Mean

sum_of_num = 0

for mark in marks:
    sum_of_num = sum_of_num + mark

mean = sum_of_num / num_count
print(f"The mean of {marks} is {mean}")
