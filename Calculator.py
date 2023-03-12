print("Welcome to Calculator 1.0!")
print("List of Things to do: ")
print("Subtraction            (s)")
print("Addition               (a)")
print("Multiplication         (m)")
print("Division               (d)")
print("Squared                (q)")

menu_decision: str = input("Type the letter: ")
var1: str = input("Please enter #1: ")
var1 = float(var1)
var2: str = input("Please enter second number: ")
var2: float = float(var2)

if menu_decision == "s":
    subtracted_num = var1 - var2
    print("Difference: " + subtracted_num)
elif menu_decision == "a":
    added_num = var1 + var2
    print("Sum: " + added_num)
elif menu_decision == "m":
    multiplied_num = var1 * var2
    print("Product: " + multiplied_num)
elif menu_decision == "d":
    if var2 == 0.0:
        print("Number is Undefined")
    elif var2 != 0.0:
        divided_num = var2 / var1
        print("Quotient: " + divided_num)
elif menu_decision == 'q':
    squared_num: float = var1 * var1
    print("Squared Number of #1: ")
    print(squared_num)
    squared_num2: float = var2
