# Dictionary is
# dict_name = [key : value, so on so forth]

num = [10, 10, 12, 12, 12, 13, 14]
num_set = {10, 12, 13, 14}  # You can NEVER repeat the SAME number in COde but USER Input can keep repeating num although code will illiminate value that is repeating

country_population_di = {"China": 15, "India": 16, "USA": 14, "Canada": 4, "Mexico": 16}

# country_population_di.pop("China")

# for country_name in country_population_di:
#     print(country_name, country_population_di[country_name])
# Instead of using this way
# You can also use this way
for key, value in country_population_di:
    print(key, value)

"""
Step 1: Loop each number to the list
Step 2: Check if the number is in the dictionary 
Step 3: If the number is in the dictionary, increment the value by 1
Step 3: If the number is in the dictionary, add the number as a set value to 1

Ex:
    
Di = {
    "number of 10s": 2
    etc.
"""
