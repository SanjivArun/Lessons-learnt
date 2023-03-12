nums_list = [10, 10, 12, 12, 12, 13, 14]

freq_dict = {}

for num in nums_list:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1
