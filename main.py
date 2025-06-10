"""
Filename: functions_and_recursion_assignment.py
Description: This script demonstrates the use of functions in Python, including:
- simple functions with parameters,
- default parameters,
- variable-length arguments,
- and recursion.

This assignment is part of my Cognizant Externship.

Jordan Wang
6/10/2025
"""

# Task 1 - Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

# Example usage for Task 1
greet_user("Alice")
sum_result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {sum_result}.")


# Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage for Task 2
describe_pet("Buddy")
describe_pet("Whiskers", "cat")


# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Example usage for Task 3
make_sandwich("Lettuce", "Tomato", "Cheese")


# Task 4 - Understanding Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage for Task 4
fact = factorial(5)
fib = fibonacci(6)
print(f"Factorial of 5 is {fact}.")
print(f"The 6th Fibonacci number is {fib}.")
