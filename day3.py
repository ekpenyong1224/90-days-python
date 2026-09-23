# Day3 - Super calculator

from sys import modules


print("--- My SUPER CALCULATOR ---")

# Get numbers from users
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))

# Do all operations

addition = num1 + num2 
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1 % num2
power = num1 ** num2
# print results with f- string

print(f"\nResults for {num1} and {num2}:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Remainder: {num1} % {num2} = {remainder}")
print(f"Power: {num1} ** {num2} = {power}")   # type: ignore

# Comparison
print(f"\nIs {num1} greater than {num2}? {num1 > num2}")
print(f"Are they equal? {num1 == num2}")
print(f"Is {num1} even? {num1 % 2 == 0}")

