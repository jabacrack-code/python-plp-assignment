# This program entails: 
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

# Step 1: ask user to enter numbers and an operation
number1 = float(input("Hello user. Please input the first number: "))
number2 = float(input("Hello user. Please input the second number: "))
operation = input("Enter either of the following operation (+, -, *, /): ")
# Step 2: Perform the operation
if operation == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")