# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User's choice for the operation
choice = input("Enter choice (1/2/3/4): ")

if choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Please select a valid operation.")
else:
    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    else:
        result = divide(num1, num2)
        operator = '/'

    print(f"{num1} {operator} {num2} = {result}")
