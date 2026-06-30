# 📝 Python Strings

> Strings are one of the most commonly used data types in Python. This document covers string creation, common methods, and different ways to combine strings.

---

# 📚 What is a String?

A **string** is a sequence of characters enclosed in quotes.

```python
name = "Python"
```

You can use:

```python
"Hello"
'Hello'
```

or

```python
"""Multi-line
String"""
```

---

# 📏 String Length

Use `len()` to get the number of characters.

```python
text = "Python"

print(len(text))
```

Output

```text
6
```

---

# 🔠 Change Letter Case

## Uppercase

```python
text = "python"

print(text.upper())
```

Output

```text
PYTHON
```

---

## Lowercase

```python
text = "PYTHON"

print(text.lower())
```

---

## Capitalize

```python
text = "python"

print(text.capitalize())
```

Output

```text
Python
```

---

## Title Case

```python
text = "hello world"

print(text.title())
```

Output

```text
Hello World
```

---

# ✂ Remove Spaces

## strip()

Removes spaces from both sides.

```python
text = "  Python  "

print(text.strip())
```

---

## lstrip()

```python
text.lstrip()
```

---

## rstrip()

```python
text.rstrip()
```

---

# 🔍 Searching

## find()

Returns the index of the first occurrence.

```python
text = "Hello Python"

print(text.find("Python"))
```

---

## count()

Counts occurrences.

```python
text = "banana"

print(text.count("a"))
```

Output

```text
3
```

---

## startswith()

```python
filename = "photo.png"

print(filename.startswith("photo"))
```

---

## endswith()

```python
print(filename.endswith(".png"))
```

---

# 🔄 Replace

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

---

# ✂ Split

Convert a string into a list.

```python
text = "Python,Java,C++"

print(text.split(","))
```

Output

```python
['Python', 'Java', 'C++']
```

---

# 🔗 Join

Join a list into a string.

```python
languages = ["Python", "Java", "C++"]

print(", ".join(languages))
```

Output

```text
Python, Java, C++
```

---

# ✔ Check String Content

## isalpha()

```python
"Python".isalpha()
```

---

## isdigit()

```python
"123".isdigit()
```

---

## isalnum()

```python
"Python123".isalnum()
```

---

## isspace()

```python
"   ".isspace()
```

---

# 🔀 Slice

## Slice Strings With Brackets [m,n,step]

```python
name = "Alireza Fahimi"
printe(name[0])
```

Output

```python
'A'
```

name = "Alireza Fahimi"
```python
print(name[1:5])
```

Output

```python
'lirez'
```

name = "Alireza Fahimi"
```python
printe(name[-1])
```

Output

```python
'i'
```

---

# 🔀 String Concatenation

## Method 1: +

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

---

## Method 2: +=

```python
text = "Hello"

text += " Python"
```

---

## Method 3: f-Strings ⭐ (Recommended)

```python
name = "Alireza"
age = 24

print(f"My name is {name} and I am {age} years old.")
```

---

## Method 4: format()

```python
print("My name is {}.".format(name))
```

---

## Method 5: % Formatting (Old Style)

```python
print("My name is %s" % name)
```

---

# 📊 Comparison of String Formatting

| Method     | Recommended | Readability |
| ---------- | ----------- | ----------- |
| `+`        | ⭐⭐          | Medium      |
| `+=`       | ⭐⭐          | Medium      |
| `f""`      | ⭐⭐⭐⭐⭐       | Excellent   |
| `format()` | ⭐⭐⭐         | Good        |
| `%`        | ⭐           | Legacy      |

---

# ⚠ Common Mistakes

Trying to concatenate a string with an integer.

```python
age = 24

print("Age: " + age)
```

❌ Error

Correct

```python
print("Age: " + str(age))
```

or

```python
print(f"Age: {age}")
```

---

# ✅ Best Practices

✔ Prefer **f-Strings** for formatting.

✔ Use `join()` instead of repeated `+` when combining many strings.

✔ Use `strip()` when processing user input.

✔ Use `lower()` or `casefold()` before comparing user input.

---

# 🧪 Practice

Write a program that:

* Gets the user's name.
* Removes extra spaces.
* Converts the name to title case.
* Prints a welcome message using an f-string.

Example:

```python
name = input("Name: ")

name = name.strip().title()

print(f"Welcome, {name}!")
```

---

# 📝 Summary

* Strings are immutable sequences of characters.
* Python provides many built-in string methods.
* `split()` converts a string into a list.
* `join()` converts a list into a string.
* `replace()` replaces text.
* `find()` searches inside a string.
* `strip()` removes surrounding spaces.
* **f-Strings are the recommended way to format strings.**

---

## 📚 Most Important Methods

| Method         | Purpose                   |
| -------------- | ------------------------- |
| `upper()`      | Uppercase                 |
| `lower()`      | Lowercase                 |
| `title()`      | Title Case                |
| `capitalize()` | Capitalize first letter   |
| `strip()`      | Remove surrounding spaces |
| `replace()`    | Replace text              |
| `split()`      | Convert to list           |
| `join()`       | Join list into string     |
| `find()`       | Find text                 |
| `count()`      | Count occurrences         |
| `startswith()` | Check prefix              |
| `endswith()`   | Check suffix              |
| `isalpha()`    | Only letters              |
| `isdigit()`    | Only digits               |
| `isalnum()`    | Letters and digits        |
| `isspace()`    | Only spaces               |

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide

---

## 📅 Last Updated

2026-06-29

---

## ⭐ Difficulty

🟢 Beginner

---

> 📖 Next Topic: Comparison Operators
