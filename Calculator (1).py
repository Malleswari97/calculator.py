def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Select an operation (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice. Please select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        operator = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operator = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operator = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operator = "/"

    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
