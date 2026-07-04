# 📝 Conditional Statements in Python

> Conditional statements allow a program to make decisions based on one or more conditions.

---

# 📚 What are Conditional Statements?

A **Conditional Statement** executes different blocks of code depending on whether a condition is `True` or `False`.

Python provides four main conditional keywords:

* `if`
* `elif`
* `else`
* Nested `if`

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# 🔹 The `if` Statement

The `if` statement executes a block of code only when its condition is `True`.

Syntax

```python
if condition:
    # code
```

Example

```python
age = 18

if age >= 18:
    print("You can vote.")
```

Output

```text
You can vote.
```

---

# 🔹 The `else` Statement

The `else` block runs when the `if` condition is `False`.

Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```text
Minor
```

---

# 🔹 The `elif` Statement

Use `elif` to check multiple conditions.

Example

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

Output

```text
Grade B
```

Python checks the conditions from top to bottom and stops after the first `True` condition.

---

# 🔹 Nested `if`

You can place an `if` statement inside another `if`.

Example

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
```

Output

```text
You can drive.
```

---

# 🔗 Using Logical Operators

Conditional statements often use logical operators.

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed.")
```

---

Using `or`

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted.")
```

---

Using `not`

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in.")
```

---

# 🎯 Comparison Operators in Conditions

Conditions usually use comparison operators.

```python
temperature = 30

if temperature > 25:
    print("It's hot.")
```

Other examples

```python
price == 100
age >= 18
score != 0
name == "Python"
```

---

# 📝 Indentation

Python uses indentation (spaces) to define code blocks.

Correct

```python
age = 20

if age >= 18:
    print("Adult")
```

Incorrect

```python
age = 20

if age >= 18:
print("Adult")
```

This raises an `IndentationError`.

---

# ⚡ Conditional Expression (Ternary Operator)

Python provides a short form for simple conditions.

Syntax

```python
value_if_true if condition else value_if_false
```

Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```text
Adult
```

---

# 📚 Multiple Conditions

Example

```python
age = 25
country = "Canada"

if age >= 18 and country == "Canada":
    print("Eligible")
```

---

# 💡 Real-World Examples

### Login Check

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid credentials.")
```

---

### Even or Odd

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### Positive, Negative, or Zero

```python
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

# ⚠ Common Mistakes

Using `=` instead of `==`

Wrong

```python
if age = 18:
    print("Adult")
```

Correct

```python
if age == 18:
    print("Adult")
```

---

Forgetting indentation

Wrong

```python
if True:
print("Hello")
```

Correct

```python
if True:
    print("Hello")
```

---

# ✅ Best Practices

✔ Keep conditions simple and readable.

✔ Avoid deeply nested `if` statements.

✔ Use `elif` instead of multiple unrelated `if` statements when only one branch should run.

✔ Use meaningful Boolean variable names.

✔ Use the ternary operator only for simple expressions.

---

# 📚 Conditional Statements Cheat Sheet

| Statement          | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `if`               | Execute code when a condition is true      |
| `elif`             | Check another condition                    |
| `else`             | Execute when no previous condition is true |
| Nested `if`        | Place an `if` inside another `if`          |
| Ternary Expression | Write a simple condition in one line       |

---

# 📝 Summary

* Conditional statements control the flow of a program.
* `if` executes code when a condition is true.
* `elif` allows checking multiple conditions.
* `else` handles all remaining cases.
* Nested `if` statements allow more detailed decision-making.
* The ternary expression is useful for simple one-line conditions.
* Proper indentation is required in Python.

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

> 📖 Next Topic: Loops (`for` and `while`)
