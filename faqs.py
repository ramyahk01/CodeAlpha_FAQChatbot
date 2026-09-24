# FAQ data for Python Programming Chatbot
# Each entry has a "question" and an "answer"

FAQS = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its simple and readable syntax. It was created by Guido van Rossum in 1991 and is widely used in web development, data science, AI, and automation."
    },
    {
        "question": "How do I install Python?",
        "answer": "Download Python from python.org, run the installer, and make sure to check 'Add Python to PATH' during installation. After installation, verify it by typing 'python --version' in the terminal."
    },
    {
        "question": "What is a variable in Python?",
        "answer": "A variable is a named container used to store data values. In Python, you don't need to declare a type; just assign a value like x = 10 or name = 'Alice'."
    },
    {
        "question": "What are the data types in Python?",
        "answer": "Main Python data types: int (whole numbers), float (decimals), str (text), bool (True/False), list, tuple, set, and dict (dictionary)."
    },
    {
        "question": "What is a list in Python?",
        "answer": "A list is an ordered, mutable collection of items, written with square brackets, e.g., numbers = [1, 2, 3]. You can add, remove, and change items."
    },
    {
        "question": "What is a tuple in Python?",
        "answer": "A tuple is an ordered, immutable collection of items, written with parentheses, e.g., point = (3, 4). Once created, its values cannot be changed."
    },
    {
        "question": "What is a dictionary in Python?",
        "answer": "A dictionary stores key-value pairs inside curly braces, e.g., person = {'name': 'Alice', 'age': 20}. It is used to look up values quickly using keys."
    },
    {
        "question": "What is the difference between a list and a tuple?",
        "answer": "Lists are mutable (can be changed) and use square brackets. Tuples are immutable (cannot be changed) and use parentheses. Tuples are faster and safer when data should not change."
    },
    {
        "question": "What is a function in Python?",
        "answer": "A function is a reusable block of code defined with 'def'. Example: def greet(name): return 'Hello ' + name. Functions help avoid repeating code."
    },
    {
        "question": "What is a loop in Python?",
        "answer": "A loop repeats a block of code. Python has 'for' loops (used with sequences) and 'while' loops (repeat while a condition is True)."
    },
    {
        "question": "What is the difference between for and while loop?",
        "answer": "'for' loops iterate over a sequence (like a list or range). 'while' loops repeat as long as a condition is True. Use 'for' when you know how many times to loop."
    },
    {
        "question": "What is an if statement in Python?",
        "answer": "An if statement runs a block of code only when a condition is True. Example: if x > 5: print('big'). You can add 'elif' and 'else' for other cases."
    },
    {
        "question": "What is indentation in Python?",
        "answer": "Indentation (spaces at the start of a line) defines blocks of code in Python. Unlike other languages, Python uses indentation instead of curly braces to group code."
    },
    {
        "question": "What is a module in Python?",
        "answer": "A module is a file containing Python code that can be imported into other files. Example: import math gives access to math.sqrt(), math.pi, etc."
    },
    {
        "question": "What is the difference between a module and a package?",
        "answer": "A module is a single .py file. A package is a folder containing multiple modules and an __init__.py file. Packages help organize related modules."
    },
    {
        "question": "How do I install a Python package?",
        "answer": "Use pip, Python's package manager. Example: pip install requests. To see installed packages, use pip list."
    },
    {
        "question": "What is pip?",
        "answer": "pip is Python's package installer. It downloads and installs third-party libraries from PyPI (Python Package Index). Example: pip install numpy."
    },
    {
        "question": "What is a virtual environment?",
        "answer": "A virtual environment is an isolated Python environment for a project. It keeps that project's packages separate so different projects don't conflict. Create one with: python -m venv venv"
    },
    {
        "question": "What is exception handling in Python?",
        "answer": "Exception handling uses try, except, else, and finally blocks to catch and handle errors so your program doesn't crash. Example: try: x = 1/0 except ZeroDivisionError: print('Cannot divide by zero')."
    },
    {
        "question": "What is object oriented programming in Python?",
        "answer": "OOP organizes code using classes and objects. A class is a blueprint; an object is an instance. It supports encapsulation, inheritance, and polymorphism. Example: class Dog: def bark(self): print('Woof')."
    },
]