# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to get user input for numbers and operation
def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            op = input("Enter operation (+, -, *, /): ")
            if op not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operation")
            break
        except ValueError as e:
            print("Invalid input. Please enter valid numbers and operation.")
            print(e)
    return num1, num2, op

# Function to perform calculation based on operation choice
def calculate(num1, num2, op):
    if op == '+':
        return add(num1, num2)
    elif op == '-':
        return subtract(num1, num2)
    elif op == '*':
        return multiply(num1, num2)
    elif op == '/':
        return divide(num1, num2)

# Main function
def main():
    num1, num2, op = get_user_input()
    result = calculate(num1, num2, op)
    print("Result:", result)

if __name__ == "__main__":
    main()
