# 📝 Comparison Operators in Python

> Comparison operators are used to compare two values. Every comparison returns a Boolean value: `True` or `False`.

---

# 📚 What are Comparison Operators?

Comparison operators compare two values or expressions.

The result of every comparison is always a **Boolean**:

* `True`
* `False`

Example:

```python
print(10 > 5)
```

Output

```text
True
```

---

# 📋 Comparison Operators

| Operator | Meaning               | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 3` | `True` |
| `>`      | Greater than          | `8 > 2`  | `True` |
| `<`      | Less than             | `4 < 7`  | `True` |
| `>=`     | Greater than or equal | `5 >= 5` | `True` |
| `<=`     | Less than or equal    | `3 <= 6` | `True` |

---

# 🔹 Equal To (`==`)

Checks whether two values are equal.

```python
print(10 == 10)
```

Output

```text
True
```

Example

```python
username = "admin"

print(username == "admin")
```

---

# 🔹 Not Equal To (`!=`)

Checks whether two values are different.

```python
print(10 != 20)
```

Output

```text
True
```

---

# 🔹 Greater Than (`>`)

Checks whether the left value is larger.

```python
print(20 > 10)
```

Output

```text
True
```

---

# 🔹 Less Than (`<`)

Checks whether the left value is smaller.

```python
print(5 < 9)
```

Output

```text
True
```

---

# 🔹 Greater Than or Equal (`>=`)

```python
age = 18

print(age >= 18)
```

Output

```text
True
```

---

# 🔹 Less Than or Equal (`<=`)

```python
score = 65

print(score <= 100)
```

Output

```text
True
```

---

# 📚 Comparing Different Data Types

### Numbers

```python
print(10 > 5)
```

---

### Strings

Strings are compared alphabetically (lexicographical order).

```python
print("apple" < "banana")
```

Output

```text
True
```

---

### Boolean Values

```python
print(True == True)

print(True != False)
```

---

# 🔗 Chained Comparisons

Python allows multiple comparisons in a single expression.

```python
age = 25

print(18 <= age <= 30)
```

Output

```text
True
```

Instead of writing:

```python
print(age >= 18 and age <= 30)
```

---

# 🎯 Using Comparison Operators with `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# 🔄 Using Comparison Operators in Loops

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# ⚠ Comparing Strings

Comparison is based on Unicode values.

```python
print("A" < "B")
```

Output

```text
True
```

Case matters.

```python
print("apple" == "Apple")
```

Output

```text
False
```

If you want a case-insensitive comparison:

```python
name = "Python"

print(name.lower() == "python")
```

---

# ⚠ Comparing Lists

```python
print([1, 2] == [1, 2])
```

Output

```text
True
```

Order matters.

```python
print([1, 2] == [2, 1])
```

Output

```text
False
```

---

# ❌ Common Mistakes

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

Comparing different data types.

```python
print("5" == 5)
```

Output

```text
False
```

Convert the value first.

```python
print(int("5") == 5)
```

---

# 💡 Best Practices

✔ Use `==` to compare values.

✔ Use `=` only for assignment.

✔ Use chained comparisons when appropriate.

✔ Normalize strings (`lower()` or `casefold()`) before comparing user input.

✔ Compare values of the same data type whenever possible.

---


# 📚 Comparison Operators Cheat Sheet

| Operator | Description           |
| -------- | --------------------- |
| `==`     | Equal to              |
| `!=`     | Not equal to          |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

---

# 📝 Summary

* Comparison operators compare two values.
* Every comparison returns either `True` or `False`.
* They are commonly used in conditions and loops.
* Python supports chained comparisons for cleaner code.
* Always use `==` for comparison and `=` for assignment.
* Be careful when comparing different data types or strings with different letter cases.

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

> 📖 Next Topic: Logical Operators (`and`, `or`, `not`)
