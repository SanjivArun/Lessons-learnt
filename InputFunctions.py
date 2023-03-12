first_name = input("Please input your first name? ")

tip = "If you don't have middle name, just click enter!"
middle_name = input("Middle Name?")

last_name = input("Last name? ")

user_age = input("Please type your current age: ")

print("Name: " + last_name + ", " + first_name)
print("Middle Name: " + middle_name)
user_age = int(user_age) + 5
print("Age in 5 years: " + str(user_age))
