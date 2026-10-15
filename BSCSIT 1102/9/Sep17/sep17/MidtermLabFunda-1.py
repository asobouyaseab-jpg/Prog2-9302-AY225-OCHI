"""
College-Level Python Examples
Author: Sir Val
Purpose: Demonstrate key Python concepts using menu-driven examples.

"""
import math
import random
import time


# =========================
# FUNCTIONS FOR EACH TOPIC
# =========================

# 1. Function Definitions and Parameters
def topic_functions():
    print("\n=== 1. Function Definitions and Parameters ===")

    def greet(name):
        """Simple greeting function"""
        print(f"Hello, {name}! Welcome to Python programming.")

    def add_numbers(a, b):
        """Returns the sum of two numbers"""
        return a + b

    def power(base, exponent=2):
        """Raises base to the power of exponent"""
        return base ** exponent

    print("\n[Program 1] Greeting Function:")
    greet("Alice")

    print("\n[Program 2] Add Numbers Function:")
    print(f"The sum is: {add_numbers(5, 10)}")

    print("\n[Program 3] Power Function with Default Parameter:")
    print("5 squared:", power(5))
    print("5 cubed:", power(5, 3))


# 2. Scope and Lifetime of Variables
def topic_scope():
    print("\n=== 2. Scope and Lifetime of Variables ===")

    x = 10  # Global variable

    def modify_variable():
        x = 5  # Local variable
        print(f"Inside function, x = {x}")

    print("\n[Program 1] Local vs Global Variables:")
    modify_variable()
    print(f"Outside function, x = {x}")
    global count
    count = 0

    def increment():
        nonlocal_count = 0  # Demonstrating function-local variable

    print("\n[Program 2] Global Keyword Usage:")
   
    count = 0
    def increment_global():
        global count
        count += 1
    increment_global()
    increment_global()
    print(f"Count after increments: {count}")

    print("\n[Program 3] Lifetime of Variables:")
    def temp_storage():
        message = "I exist only inside this function!"
        print(message)
    temp_storage()


# 3. Built-in Functions vs. User-Defined Functions
def topic_builtin_vs_user():
    print("\n=== 3. Built-in Functions vs. User-Defined Functions ===")

    numbers = [5, 9, 1, 7]

    print("\n[Program 1] Using Built-in max():")
    print("Maximum number:", max(numbers))

    def my_max(lst):
        maximum = lst[0]
        for num in lst:
            if num > maximum:
                maximum = num
        return maximum

    print("\n[Program 2] Using User-Defined max():")
    print("Maximum number:", my_max(numbers))

    print("\n[Program 3] Performance Comparison:")
    numbers = list(range(1, 100000))
    start = time.time()
    max(numbers)
    end = time.time()
    print(f"Built-in function took {end - start:.6f} seconds")

    start = time.time()
    my_max(numbers)
    end = time.time()
    print(f"User-defined function took {end - start:.6f} seconds")


# 4. Modules and Libraries
def topic_modules():
    print("\n=== 4. Modules and Libraries ===")

    print("\n[Program 1] math Module:")
    radius = 5
    area = math.pi * math.pow(radius, 2)
    print(f"Area of circle with radius {radius}: {area:.2f}")

    print("\n[Program 2] random Module:")
    print("Random number between 1 and 10:", random.randint(1, 10))

    print("\n[Program 3] Custom Module Simulation:")
    # Instead of an external file, simulate custom module
    def greet_module(name):
        return f"Hello, {name} from my custom module!"
    print(greet_module("Alice"))


# 5. Lists, Tuples, and Sets
def topic_lists_tuples_sets():
    print("\n=== 5. Lists, Tuples, and Sets ===")

    print("\n[Program 1] List Example:")
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    fruits.remove("banana")
    fruits.sort()
    print(fruits)

    print("\n[Program 2] Tuple Example:")
    coordinates = (10, 20)
    print("X:", coordinates[0], "Y:", coordinates[1])

    print("\n[Program 3] Set Example:")
    numbers = {1, 2, 2, 3, 4, 4, 5}
    print(numbers)


# 6. Dictionaries and Their Applications
def topic_dictionaries():
    print("\n=== 6. Dictionaries and Their Applications ===")

    print("\n[Program 1] Simple Dictionary:")
    student = {"name": "Alice", "age": 21, "course": "CS"}
    print(f"{student['name']} is taking {student['course']}.")

    print("\n[Program 2] Iterating Over Dictionary:")
    grades = {"Math": 95, "Science": 88, "English": 90}
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

    print("\n[Program 3] Word Counter Application:")
    text = "python is fun and python is powerful"
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)


# 7. List Comprehensions
def topic_list_comprehensions():
    print("\n=== 7. List Comprehensions ===")

    print("\n[Program 1] Basic List Comprehension:")
    squares = [x**2 for x in range(1, 6)]
    print(squares)

    print("\n[Program 2] Filtering with List Comprehension:")
    numbers = [10, 15, 20, 25, 30]
    evens = [n for n in numbers if n % 2 == 0]
    print(evens)

    print("\n[Program 3] Nested List Comprehension:")
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(matrix)


# =========================
# MENU-DRIVEN INTERFACE
# =========================

def main():
    while True:
        print("\n====== Python Concept Explorer ======")
        print("1. Function Definitions and Parameters")
        print("2. Scope and Lifetime of Variables")
        print("3. Built-in Functions vs. User-Defined Functions")
        print("4. Modules and Libraries")
        print("5. Lists, Tuples, and Sets")
        print("6. Dictionaries and Their Applications")
        print("7. List Comprehensions")
        print("0. Exit")

        choice = input("Select a topic (0-7): ")

        if choice == "1":
            topic_functions()
        elif choice == "2":
            topic_scope()
        elif choice == "3":
            topic_builtin_vs_user()
        elif choice == "4":
            topic_modules()
        elif choice == "5":
            topic_lists_tuples_sets()
        elif choice == "6":
            topic_dictionaries()
        elif choice == "7":
            topic_list_comprehensions()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
