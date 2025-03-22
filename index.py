# Display a welcome message to the user
print('Give me two numbers and a mathematical operation, and I will calculate the result for you.')

# Take input for the first number from the user
num1 = input('Enter the first number: ')
num1 = float(num1)  # Convert the input from string to float
print(f"First number entered: {num1}")  # Display the entered number

# Take input for the second number from the user
num2 = input('Enter the second number: ')
num2 = float(num2)  # Convert the input from string to float
print(f"Second number entered: {num2}")  # Display the entered number

# Ask the user for the mathematical operation to perform
operation = input('Enter the operation you want to perform (+, -, *, /): ')

# Perform the calculation based on the selected operation
if operation == '+':
    print("The addition of the two numbers is:", num1 + num2)
elif operation == '-':
    print("The subtraction of the two numbers is:", num1 - num2)
elif operation == '*':
    print("The multiplication of the two numbers is:", num1 * num2)
elif operation == '/':
    print("The division of the two numbers is:", num1 / num2)
else:
    # If the user enters an invalid operation, display an error message
    print('Invalid operation')
