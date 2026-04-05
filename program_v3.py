# ============================================================
# Student Calculator - Version 3
# Description: Added user input and interactive menu
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("=== Student Calculator v3 ===")
    print("Select operation:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Exit")

    while True:
        choice = input("\nEnter choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        else:
            print("Invalid input. Please enter 1-5.")

calculator()
