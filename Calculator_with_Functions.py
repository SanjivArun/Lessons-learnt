print("Welcome to Math Calculator 2.0 ")

num_1 = int(input("Enter your first Number: "))
num_2 = int(input("Enter your second Number: "))


def remainder(a, b):
    if b == 0:
        return print("Undefined")
    return a % b


def exponent(a, b):
    return a ** b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return print("Undefined")
    return a / b


def multiply(a, b):
    return a * b


print("First NUM: ", num_1)
print("Second NUM: ", num_2)
print("Subtract             (s)")
print("Add                  (a)")
print("Divide               (d)")
print("Exponent             (e)")
print("Multiply             (m)")
print("Remainder            (r)")
menu_drop = str(input("Now what would you like to do?"))

print("Answer: ")

if menu_drop == "s":
    subtract(num_1, num_2)

elif menu_drop == "a":
    add(num_1, num_2)

elif menu_drop == "d":
    divide(num_1, num_2)

elif menu_drop == "e":
    exponent(num_1, num_2)

elif menu_drop == "m":
    multiply(num_1, num_2)

elif menu_drop == "r":
    remainder(num_1, num_2)

else:
    print("Error 475: Error within INPUT")
