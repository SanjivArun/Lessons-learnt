import math
marks = []

print("Program to find ODD or EVEN")
input_count = int(input("How many numbers you WANT to check? "))

for i in range(0, input_count):
    num = int(input("Enter a num: "))
    marks.append(num)
    # You can use marks.insert which keeps the number in the front

for m in marks:
    if m % 2 == 0:
        print(m, " Is even num")
    else:
        print(m, " Is ODD num")
