# 📝 Loops in Python

> Loops allow you to execute a block of code repeatedly without writing the same code multiple times.

---

# 📚 What are Loops?

A **loop** is a programming structure that repeats a block of code until a condition is no longer satisfied or until all items in a sequence have been processed.

Python provides two main loop types:

* `for`
* `while`

Loops are commonly used for:

* Processing lists and dictionaries
* Reading files
* Repeating tasks
* User input validation
* Data analysis

---

# 🔹 The `for` Loop

A `for` loop iterates over a sequence such as a list, tuple, string, dictionary, or range.

Syntax

```python
for item in sequence:
    # code
```

Example

```python
languages = ["Python", "Java", "Go"]

for language in languages:
    print(language)
```

Output

```text
Python
Java
Go
```

---

# 🔹 Using `range()`

The `range()` function generates a sequence of numbers.

### From 0 to 4

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

---

### Start and Stop

```python
for i in range(1, 6):
    print(i)
```

Output

```text
1
2
3
4
5
```

---

### Start, Stop, Step

```python
for i in range(0, 10, 2):
    print(i)
```

Output

```text
0
2
4
6
8
```

---

# 🔹 Looping Through a String

```python
text = "Python"

for char in text:
    print(char)
```

---

# 🔹 Looping Through a Dictionary

Loop through keys

```python
person = {
    "name": "Alireza",
    "age": 24
}

for key in person:
    print(key)
```

Loop through values

```python
for value in person.values():
    print(value)
```

Loop through key-value pairs

```python
for key, value in person.items():
    print(key, value)
```

---

# 🔹 The `while` Loop

A `while` loop continues executing as long as its condition is `True`.

Syntax

```python
while condition:
    # code
```

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

---

# 🔹 Infinite Loops

A `while` loop can run forever if its condition never becomes `False`.

```python
while True:
    print("Running...")
```

⚠️ Be careful. Use `Ctrl + C` in the terminal to stop an infinite loop.

---

# 🔹 The `break` Statement

`break` immediately exits the loop.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Output

```text
0
1
2
3
4
```

---

# 🔹 The `continue` Statement

`continue` skips the current iteration.

```python
for number in range(6):
    if number == 3:
        continue

    print(number)
```

Output

```text
0
1
2
4
5
```

---

# 🔹 The `pass` Statement

`pass` is a placeholder that does nothing.

```python
for number in range(5):
    pass
```

Useful when writing code incrementally.

---

# 🔹 The `else` Clause in Loops

Both `for` and `while` can have an `else` block.

```python
for i in range(3):
    print(i)
else:
    print("Loop finished.")
```

Output

```text
0
1
2
Loop finished.
```

The `else` block runs only if the loop finishes normally (without `break`).

---

# 🔹 Nested Loops

A loop can contain another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# 🔹 Using `enumerate()`

Get both the index and value while looping.

```python
languages = ["Python", "Java", "Go"]

for index, language in enumerate(languages):
    print(index, language)
```

Output

```text
0 Python
1 Java
2 Go
```

---

# 🔹 Using `zip()`

Iterate over multiple sequences together.

```python
names = ["Ali", "Sara", "Reza"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(name, score)
```

Output

```text
Ali 90
Sara 85
Reza 95
```

---

# 💡 Real-World Examples

### Calculate the Sum of Numbers

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output

```text
15
```

---

### Search for an Item

```python
languages = ["Python", "Java", "Go"]

for language in languages:
    if language == "Go":
        print("Found!")
        break
```

---

### Password Validation

```python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted.")
```

---

# ⚠ Common Mistakes

### Forgetting to update the loop variable

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

This creates an infinite loop.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

### Modifying a list while iterating over it

Avoid changing a list directly inside a loop unless you understand the consequences.

---

# ✅ Best Practices

✔ Use `for` when iterating over a sequence.

✔ Use `while` when the number of iterations is unknown.

✔ Use `break` to exit early when appropriate.

✔ Use `continue` to skip unnecessary work.

✔ Prefer `enumerate()` over manually tracking indexes.

✔ Avoid unnecessary nested loops.

---


# 📚 Loop Keywords Cheat Sheet

| Keyword / Function | Description                            |
| ------------------ | -------------------------------------- |
| `for`              | Iterate over a sequence                |
| `while`            | Repeat while a condition is true       |
| `range()`          | Generate a sequence of numbers         |
| `break`            | Exit the loop immediately              |
| `continue`         | Skip the current iteration             |
| `pass`             | Placeholder statement                  |
| `enumerate()`      | Get both index and value               |
| `zip()`            | Iterate over multiple sequences        |
| `else`             | Execute after a loop finishes normally |

---

# 📝 Summary

* Python provides two loop types: `for` and `while`.
* `for` loops iterate over sequences.
* `while` loops continue until a condition becomes `False`.
* `range()` generates numeric sequences.
* `break` exits a loop early.
* `continue` skips the current iteration.
* `enumerate()` and `zip()` make loops cleaner and more readable.
* Be careful to avoid infinite loops with `while`.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟢 Beginner

---

> 📖 Next Topic: Functions
