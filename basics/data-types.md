# 📝 Data Types in Python

> Data types define the kind of value a variable can store.

---

# 📚 What is a Data Type?

Every value in Python has a **data type**.

The data type determines:

* What kind of data is stored.
* What operations can be performed on it.
* How Python handles the value.

Example:

```python
age = 25
```

The value `25` has the data type **int**.

---

# 🧩 Built-in Data Types

| Category | Data Type  | Example                |
| -------- | ---------- | ---------------------- |
| Numeric  | int        | `10`                   |
| Numeric  | float      | `3.14`                 |
| Numeric  | complex    | `2+3j`                 |
| Text     | str        | `"Python"`             |
| Boolean  | bool       | `True`                 |
| Sequence | list       | `[1, 2, 3]`            |
| Sequence | tuple      | `(1, 2, 3)`            |
| Sequence | range      | `range(5)`             |
| Mapping  | dict       | `{"name": "Ali"}`      |
| Set      | set        | `{1, 2, 3}`            |
| Set      | frozenset  | `frozenset({1,2})`     |
| Binary   | bytes      | `b"Hello"`             |
| Binary   | bytearray  | `bytearray(5)`         |
| Binary   | memoryview | `memoryview(bytes(5))` |
| Special  | NoneType   | `None`                 |

---

# 🔢 Numeric Types

## Integer (int)

Whole numbers without decimals.

```python
age = 24
```

---

## Float

Numbers with decimal points.

```python
price = 19.99
```

---

## Complex

Used for mathematical calculations.

```python
number = 3 + 4j
```

---

# 🔤 String (str)

Strings store text.

```python
language = "Python"
```

Strings can use:

```python
'Hello'
```

or

```python
"Hello"
```

or

```python
"""Multi-line
String"""
```

---

# ✅ Boolean (bool)

A Boolean value has only two possible values.

```python
True
False
```

Example

```python
is_logged_in = True
```

---

# 📋 List

A list stores multiple values.

Lists are **ordered** and **mutable**.

```python
numbers = [1, 2, 3]
```

---

# 📌 Tuple

A tuple is similar to a list.

It is **ordered** but **immutable**.

```python
coordinates = (10, 20)
```

---

# 🗂 Dictionary

Stores data as key-value pairs.

```python
student = {
    "name": "Ali",
    "age": 24
}
```

---

# 🎯 Set

Stores unique values.

```python
colors = {"red", "blue", "green"}
```

Duplicate values are automatically removed.

---

# 🚫 NoneType

Represents the absence of a value.

```python
result = None
```

---

# 🔍 Checking Data Types

Use the `type()` function.

```python
name = "Python"

print(type(name))
```

Output

```python
<class 'str'>
```

---

# 🔄 Type Conversion

Convert between data types.

```python
age = "25"

age = int(age)
```

---

Convert integer to string.

```python
number = 100

text = str(number)
```

---

Convert integer to float.

```python
price = float(50)
```

---

# ⚠ Common Mistakes

Trying to add a string and an integer.

```python
age = "20"

print(age + 5)
```

❌ Error

Correct:

```python
print(int(age) + 5)
```

---

# ✅ Best Practices

✔ Choose the correct data type.

✔ Convert values only when necessary.

✔ Use `type()` while learning.

✔ Keep variable names meaningful.

---

# 🧪 Practice

Create variables with the following data types.

```python
name = "Alireza"

age = 24

height = 1.80

is_student = False

skills = ["Python", "Git"]

location = ("Iran", "Birjand")

person = {
    "name": "Alireza",
    "age": 24
}

colors = {"Red", "Blue"}

nothing = None
```

Then print the type of each variable using:

```python
print(type(variable_name))
```

---

# 📝 Summary

* Every value in Python has a data type.
* Python has several built-in data types.
* Use `type()` to identify a value's type.
* Use type conversion functions (`int()`, `float()`, `str()`, etc.) when needed.
* Choosing the right data type makes code cleaner and more efficient.

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

> 📖 Next Topic: python Strings
