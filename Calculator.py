def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(n):
    return pow(n, 2)

def main():
    x = int(input("What's x? "))
    #print("x squared is", square(x))

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")


while True:
    choice = input("Select Operator (1, 2, 3, 4, 5): ")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

    if choice == ("5"):
        x = int(input("Enter a number: "))
        print("x squared is", square(x))
    else:

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Another Calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Let's calculate again!!")
