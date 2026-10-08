Absolutely. 🐍 Let’s learn **Python from 0 → 100**, assuming you’ve never programmed before.

I’d structure it as a **course**, not a giant dump of syntax. You’ll learn a concept, see examples, then solve exercises and build projects.

## 🐍 Python: 0 → 100 Roadmap

### Level 0: Programming Basics

You’ll learn:

* What programming actually is
* How Python works
* Installing/running Python
* `print()`
* Comments
* Errors and debugging
* Variables
* Basic data types

Example:

```python
name = "Alex"
age = 20

print("Hello", name)
print("You are", age, "years old")
```

---

### Level 10: Numbers & Strings

Learn:

```python
+  -  *  /  //  %  **
```

and:

```python
name = "Alex"

print(name.upper())
print(name.lower())
print(len(name))
```

You’ll understand strings, numbers, booleans, type conversion, and f-strings.

---

### Level 20: Conditions

Teach Python how to make decisions:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Then:

```python
if
elif
else
and
or
not
```

**Project:** 🔐 Password checker

---

### Level 30: Loops

You'll learn:

```python
for
while
range()
break
continue
```

Example:

```python
for i in range(5):
    print(i)
```

**Projects:**

* Number guessing game
* Multiplication table
* Countdown
* Simple quiz

---

### Level 40: Lists, Tuples & Sets

You'll learn how to store collections of data:

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])

fruits.append("mango")
fruits.remove("banana")
```

Then:

* Lists
* Tuples
* Sets
* Indexing
* Slicing
* Nested collections

**Project:** 🛒 Shopping-list program

---

### Level 50: Dictionaries

One of Python's most important concepts:

```python
person = {
    "name": "Alex",
    "age": 20,
    "city": "Baku"
}

print(person["name"])
```

You'll learn:

* Keys and values
* Adding/removing data
* Looping through dictionaries
* Nested dictionaries

**Project:** 📖 Contact book

---

### Level 60: Functions

This is where your programs start becoming properly organized.

```python
def greet(name):
    print("Hello", name)

greet("Alex")
```

Then:

* Parameters
* Arguments
* Return values
* Default arguments
* Scope
* `*args`
* `**kwargs`
* Lambda functions

**Project:** 🧮 Calculator

---

### Level 70: Files & Errors

You'll learn to make programs that actually remember things.

```python
with open("notes.txt", "w") as file:
    file.write("Learn Python!")
```

Then:

```python
try:
    ...
except:
    ...
```

You'll learn:

* Reading files
* Writing files
* JSON
* CSV
* Exceptions
* Debugging

**Project:** 📝 To-do list saved to a file

---

### Level 80: Object-Oriented Programming

Now we enter the big Python castle. 🏰

You'll learn:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")
```

Then:

* Classes
* Objects
* Attributes
* Methods
* `__init__`
* Inheritance
* Encapsulation
* Polymorphism

**Project:** 🎮 Text-based RPG

---

### Level 90: Professional Python

You'll learn the tools used in real projects:

* Modules
* Packages
* `pip`
* Virtual environments
* APIs
* HTTP requests
* `datetime`
* Regular expressions
* Type hints
* Testing
* Logging
* Environment variables
* Git/GitHub
* Project structure

Example API request:

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

---

### Level 100: Real-World Python 🚀

Then we specialize.

You can choose:

**🤖 AI / Machine Learning**

* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* PyTorch
* LLM APIs

**🌐 Web Development**

* Flask
* FastAPI
* Django
* Databases
* REST APIs

**📊 Data Science**

* NumPy
* Pandas
* Matplotlib
* SQL
* Statistics
* Machine learning

**⚙️ Automation**

* Web scraping
* File automation
* Excel automation
* APIs
* Bots
* Scripts

**💻 Software Development**

* Advanced OOP
* Architecture
* Testing
* Databases
* APIs
* Deployment

---

# How we'll learn

I recommend this cycle for **every topic**:

**Learn → Example → You try → Exercise → Mini-project → Review**

I won't just show you code and say "good luck, soldier." 😄

For example, when we reach `if` statements:

### Lesson

```python
age = 20

if age >= 18:
    print("You can enter.")
else:
    print("You cannot enter.")
```

### Your first challenge

Write a program that asks the user for their age and prints:

* `"Child"` if under 13
* `"Teenager"` if 13–17
* `"Adult"` if 18+

You'll write the code, send it to me, and I'll **check it, explain mistakes, and gradually make the challenges harder**.

---

# 🟢 Lesson 1: Your first Python program

Let's start at absolute zero.

Python can tell the computer to display something using `print()`:

```python
print("Hello, world!")
```

You can print numbers too:

```python
print(10)
print(25 + 5)
print(100 / 4)
```

Python calculates:

```text
25 + 5 = 30
100 / 4 = 25
```

You can also put several things together:

```python
print("My name is Alex")
print("I am", 20, "years old")
```

### Your first exercise 🎯

Write a Python program that prints **exactly three lines**:

```text
Your name
Your age
Why you want to learn Python
```

For example:

```python
print("Alex")
print(20)
print("I want to become a programmer")
```

**Send me your code**, even if you think it's wrong. We'll start from there and work our way all the way to Python 100. 🐍
