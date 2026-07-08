# 📝 Functions in Python

> Functions are reusable blocks of code that perform a specific task. They help make programs more organized, readable, and maintainable.

---

# 📚 What is a Function?

A **function** is a named block of code that runs only when it is called.

Instead of writing the same code multiple times, you can define it once and reuse it whenever needed.

Benefits of functions:

* ✅ Code reusability
* ✅ Better readability
* ✅ Easier maintenance
* ✅ Less duplication
* ✅ Better organization

---

# 🔹 Defining a Function

Use the `def` keyword.

Syntax

```python id="1qk7me"
def function_name():
    # code
```

Example

```python id="e1c6ph"
def say_hello():
    print("Hello, Python!")
```

Call the function

```python id="xk8u6w"
say_hello()
```

Output

```text id="7e1qhz"
Hello, Python!
```

---

# 🔹 Function Parameters

Parameters allow functions to receive data.

```python id="1lhh5r"
def greet(name):
    print(f"Hello, {name}!")
```

Call

```python id="7i79n6"
greet("Alireza")
```

Output

```text id="p3w2m0"
Hello, Alireza!
```

---

# 🔹 Multiple Parameters

```python id="bx3r6g"
def add(a, b):
    print(a + b)

add(5, 3)
```

Output

```text id="y3bn7z"
8
```

---

# 🔹 Returning Values

Use `return` to send a value back to the caller.

```python id="vl4v3v"
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```text id="xv9jaf"
30
```

Without `return`, the function returns `None`.

---

# 🔹 Default Parameters

Parameters can have default values.

```python id="9r0nca"
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Sara")
```

Output

```text id="c2lmja"
Hello, Guest!
Hello, Sara!
```

---

# 🔹 Keyword Arguments

Arguments can be passed by name.

```python id="q7sn1u"
def introduce(name, age):
    print(name, age)

introduce(age=24, name="Alireza")
```

---

# 🔹 Positional Arguments

Arguments can also be passed by position.

```python id="qws8s4"
introduce("Alireza", 24)
```

---

# 🔹 Variable-Length Arguments (`*args`)

Use `*args` when the number of arguments is unknown.

```python id="f4e3lr"
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4, 5)
```

Output

```text id="d4z5ov"
15
```

---

# 🔹 Keyword Variable Arguments (`**kwargs`)

Use `**kwargs` to accept any number of keyword arguments.

```python id="sk2cvy"
def profile(**data):
    print(data)

profile(name="Ali", age=24, city="Tehran")
```

Output

```text id="vjk3eo"
{'name': 'Ali', 'age': 24, 'city': 'Tehran'}
```

---

# 🔹 Lambda Functions

Anonymous one-line functions.

```python id="k4b3ps"
square = lambda x: x * x

print(square(5))
```

Output

```text id="j7jtxk"
25
```

---

# 🔹 Scope

Variables created inside a function are local.

```python id="j4my5q"
def test():
    message = "Hello"

test()

print(message)
```

Output

```text id="e3gx3s"
NameError
```

---

# 🔹 Global Variables

```python id="6qf7r5"
message = "Python"

def show():
    print(message)

show()
```

---

# 🔹 Returning Multiple Values

Python returns them as a tuple.

```python id="qvdybw"
def get_user():
    return "Alireza", 24

name, age = get_user()

print(name)
print(age)
```

---

# 🔹 Recursive Functions

A recursive function calls itself.

Example: Factorial

```python id="m9slbf"
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output

```text id="s58lrm"
120
```

---

# 🔹 Docstrings

Use docstrings to describe a function.

```python id="x03t2n"
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Access it

```python id="4o6l4g"
print(add.__doc__)
```

---

# 🔹 Type Hints

Python supports optional type hints.

```python id="jmwvbd"
def add(a: int, b: int) -> int:
    return a + b
```

Type hints improve readability and IDE support.

---

# 💡 Real-World Examples

### Check Even Numbers

```python id="8iqtv9"
def is_even(number):
    return number % 2 == 0

print(is_even(10))
```

Output

```text id="nxo0zs"
True
```

---

### Calculate Average

```python id="sjsn9m"
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30]))
```

Output

```text id="r7a1zj"
20.0
```

---

### Greeting User

```python id="s1mpzi"
def welcome(name):
    return f"Welcome {name}"

print(welcome("Sara"))
```

---

# ⚠ Common Mistakes

Forgetting `return`

Wrong

```python id="e7dqqf"
def add(a, b):
    a + b
```

Correct

```python id="jlwmwb"
def add(a, b):
    return a + b
```

---

Changing mutable default arguments

Wrong

```python id="nydk3q"
def add_item(items=[]):
    items.append(1)
    return items
```

Correct

```python id="2v33m8"
def add_item(items=None):
    if items is None:
        items = []

    items.append(1)
    return items
```

---

# ✅ Best Practices

✔ Give functions meaningful names.

✔ Keep functions short and focused.

✔ Return values instead of printing whenever possible.

✔ Use docstrings.

✔ Add type hints.

✔ Avoid global variables.

✔ Each function should have a single responsibility.

---

# 📚 Function Cheat Sheet

| Keyword / Feature | Description                     |
| ----------------- | ------------------------------- |
| `def`             | Define a function               |
| `return`          | Return a value                  |
| `*args`           | Variable positional arguments   |
| `**kwargs`        | Variable keyword arguments      |
| `lambda`          | Anonymous function              |
| `global`          | Access global variables         |
| `__doc__`         | Read a function's documentation |

---

# 📝 Summary

* Functions allow code reuse and improve organization.
* Use `def` to define a function.
* Parameters receive data, and `return` sends data back.
* Functions can have default values, keyword arguments, and variable-length arguments.
* Lambda functions are useful for simple operations.
* Type hints and docstrings improve code quality.
* Keep functions small, readable, and focused on a single task.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟡 Intermediate

---

> 📖 Next Topic: 
