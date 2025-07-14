a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Select the operation you want to perform")
ch = int(input("Enter your choice: "))

match ch:
    case 1:
        c = a + b
        print(f"Addition of {a} and {b} is {c}")
    case 2:
        c = a - b
        print(f"Subtraction of {a} and {b} is {c}")
    case 3:
        c = a * b
        print(f"Multiplication of {a} and {b} is {c}")
    case 4:
        if b != 0:
            c = a / b
            print(f"Division of {a} by {b} is {c}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:     #this is default case
        print("Invalid choice")
