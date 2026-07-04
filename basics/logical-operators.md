# 📝 Logical Operators in Python

> Logical operators are used to combine or modify Boolean expressions. They always return a Boolean value (`True` or `False`).

---

# 📚 What are Logical Operators?

Logical operators allow you to combine multiple conditions into a single expression.

Python has three logical operators:

* `and`
* `or`
* `not`

These operators work with Boolean values and comparison expressions.

Example:

```python
age = 25

print(age > 18 and age < 30)
```

Output

```text
True
```

---

# 📋 Logical Operators

| Operator | Description                                        |
| -------- | -------------------------------------------------- |
| `and`    | Returns `True` if both conditions are `True`       |
| `or`     | Returns `True` if at least one condition is `True` |
| `not`    | Reverses a Boolean value                           |

---

# 🔹 AND Operator (`and`)

The `and` operator returns `True` **only if all conditions are true**.

Syntax

```python
condition1 and condition2
```

Example

```python
age = 25

print(age > 18 and age < 30)
```

Output

```text
True
```

Another example

```python
score = 80

print(score >= 50 and score <= 100)
```

Output

```text
True
```

---

# 🔹 OR Operator (`or`)

The `or` operator returns `True` if **at least one condition is true**.

```python
age = 15

print(age < 18 or age > 60)
```

Output

```text
True
```

Example

```python
is_admin = False
is_owner = True

print(is_admin or is_owner)
```

Output

```text
True
```

---

# 🔹 NOT Operator (`not`)

The `not` operator reverses a Boolean value.

```python
is_logged_in = True

print(not is_logged_in)
```

Output

```text
False
```

Another example

```python
is_active = False

print(not is_active)
```

Output

```text
True
```

---

# 📊 Truth Table

## AND

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

## OR

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

## NOT

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

# 🔗 Combining Multiple Conditions

```python
age = 24
country = "Iran"

if age >= 18 and country == "Iran":
    print("Eligible")
```

---

Another example

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
```

---

# 🎯 Using Logical Operators with `if`

```python
temperature = 22

if temperature >= 20 and temperature <= 30:
    print("Nice weather")
```

---

# 🔄 Using Logical Operators with `while`

```python
count = 1

while count <= 5 and count > 0:
    print(count)
    count += 1
```

---

# ⚡ Short-Circuit Evaluation

Python evaluates expressions efficiently.

## AND

If the first condition is `False`, Python does not evaluate the second condition.

```python
age = 15

print(age > 18 and 10 / 0 > 1)
```

No error occurs because the second expression is never evaluated.

---

## OR

If the first condition is `True`, Python skips the second condition.

```python
print(True or 10 / 0 > 1)
```

Again, no error occurs.

---

# ⚠ Common Mistakes

Using `&` instead of `and`

Wrong

```python
if age > 18 & age < 30:
    print("OK")
```

Correct

```python
if age > 18 and age < 30:
    print("OK")
```

---

Forgetting parentheses in complex expressions.

Instead of writing long expressions without grouping, use parentheses for readability.

```python
if (age >= 18 and age <= 30) or is_admin:
    print("Access granted")
```

---

# 💡 Best Practices

✔ Keep conditions simple.

✔ Use parentheses for complex logic.

✔ Use meaningful Boolean variable names.

✔ Take advantage of Python's short-circuit evaluation.

✔ Avoid deeply nested conditions whenever possible.

---

# 📚 Logical Operators Cheat Sheet

| Operator | Description                           | Example                |
| -------- | ------------------------------------- | ---------------------- |
| `and`    | Both conditions must be `True`        | `x > 0 and x < 10`     |
| `or`     | At least one condition must be `True` | `is_admin or is_owner` |
| `not`    | Reverse a Boolean value               | `not is_logged_in`     |

---

# 📝 Summary

* Python has three logical operators: `and`, `or`, and `not`.
* Logical operators work with Boolean expressions.
* `and` requires all conditions to be true.
* `or` requires at least one condition to be true.
* `not` reverses a Boolean value.
* Python uses short-circuit evaluation to improve performance.
* Logical operators are commonly used in `if`, `while`, filtering, and validation.

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

> 📖 Next Topic: Conditional Statements (`if`, `elif`, `else`)
