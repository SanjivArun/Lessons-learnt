age = input("What is your Age? ")
age = int(age)

if age <= 12:
    print("You are a kid")
elif 12 < age <= 19:
    print("You are a teen")
elif 19 < age < 60:
    print("You are an adult!")

elif 60 <= age < 120:
    print("You are old")
else:
    print("You are seriously OLD")
