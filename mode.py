num_list = []

mode = int
num_mode_count = int

# User enters numbers
print("Find the MEAN!")  # OR len(marks)
num_count = int(input("Enter number of numbers you would like to import: "))

for m in range(0, num_count):
    num = int(input("Enter num: "))
    num_list.append(num)

# Find Mode

freq_dict = {}
num_max_freq = 0
num_max_freq_key = 0

for num in num_list:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

    if freq_dict[num] > num_max_freq:
        num_max_freq = freq_dict[num]
        num_max_freq_key = num
