# ============================================================
# Student Calculator - Version 2
# Description: Added multiply and divide operations
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

print("=== Student Calculator v2 ===")
print("Addition:       5 + 3  =", add(5, 3))
print("Subtraction:    9 - 4  =", subtract(9, 4))
print("Multiplication: 6 x 7  =", multiply(6, 7))
print("Division:       10 / 2 =", divide(10, 2))
