print('Give me two numbers and a mathematical operation, and I will calculate the result for you.')
num1 = input('Enter the first number: ')
num1=float(num1)
print(f"First number entered: {num1}")
num2 = input('Enter the second number: ')
num2=float(num2)
print(f"Second number entered: {num2}")
operation = input('Enter the operation you want to perform: ')
if operation == '+':
    print("The addition of the two numbers is:",num1 + num2)
elif operation == '-':
    print("The substraction of the two numbers is:",num1 - num2)
elif operation == '*':
    print("The multiplication of the two numbers is:",num1 * num2)
elif operation == '/':
    print("The division of the two numbers is:",num1 / num2)
else:
    print('Invalid operation')