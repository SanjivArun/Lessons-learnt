"""
mark1 = 84
mark2 = 56
mark3 = 100
mark4 = 75

average = (mark1 + mark2 + mark3 + mark4) / 4
print("AVG: " + str(average), "AVG: %.3f" % average)
"""
# marks = {84, 56, 100, 75} #Stops repeating numbers?
marks = [84, 56, 100, 75]

sum1 = 0
for mark in marks:
    sum1 = sum1 + mark

average = sum1 / len(marks)  # Length of the list
print("Avg: %.3f" % average)
