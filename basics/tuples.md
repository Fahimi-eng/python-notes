# 📝 Tuples in Python

> A tuple is an ordered, immutable collection that can store multiple values.

---

# 📚 What is a Tuple?

A **Tuple** is one of Python's built-in data structures.

It is very similar to a **List**, but unlike lists, tuples **cannot be modified after they are created**.

Example:

```python
coordinates = (35.6892, 51.3890)
```

Once a tuple is created, its items cannot be added, removed, or changed.

---

# ✨ Characteristics of Tuples

Python tuples are:

* ✅ Ordered
* ✅ Immutable (cannot be changed)
* ✅ Allow duplicate values
* ✅ Can store different data types
* ✅ Can contain nested tuples and lists
* ✅ Faster than lists for read-only data

---

# 📌 Creating Tuples

### Empty Tuple

```python
empty_tuple = ()
```

or

```python
empty_tuple = tuple()
```

---

### Tuple with Values

```python
numbers = (10, 20, 30)
```

---

### Mixed Data Types

```python
person = ("Alireza", 24, True, 1.80)
```

---

### Single-Item Tuple

⚠ A comma is required.

```python
value = (5,)
```

Without the comma:

```python
value = (5)
```

This is an integer, **not** a tuple.

---

# 🎯 Accessing Tuple Items

```python
languages = ("Python", "Java", "Go")
```

First item

```python
languages[0]
```

Last item

```python
languages[-1]
```

---

# ✂ Slicing

```python
numbers = (10, 20, 30, 40, 50)
```

First three items

```python
numbers[:3]
```

Last two items

```python
numbers[-2:]
```

---

# 🔁 Iterating Through a Tuple

```python
for language in languages:
    print(language)
```

---

Using `enumerate()`

```python
for index, language in enumerate(languages):
    print(index, language)
```

---

# 📏 Tuple Length

```python
len(languages)
```

---

# 🔍 Checking Membership

```python
"Python" in languages
```

---

# 📚 Useful Tuple Methods

Unlike lists, tuples have only two built-in methods.

## count()

Counts how many times a value appears.

```python
numbers = (1, 2, 2, 3, 2)

numbers.count(2)
```

Output

```text
3
```

---

## index()

Returns the index of the first matching value.

```python
numbers.index(3)
```

Output

```text
3
```

---

# 🔄 Packing and Unpacking

## Tuple Packing

```python
person = ("Alireza", 24, "Python")
```

---

## Tuple Unpacking

```python
name, age, language = person

print(name)
print(age)
print(language)
```

Output

```text
Alireza
24
Python
```

---

# ⭐ Swapping Variables

One of Python's most useful features.

```python
x = 10
y = 20

x, y = y, x
```

Output

```python
print(x)
print(y)
```

```text
20
10
```

---

# 🪆 Nested Tuples

```python
matrix = (
    (1, 2),
    (3, 4)
)
```

Access an item

```python
matrix[1][0]
```

Output

```text
3
```

---

# 📋 Tuple vs List

| Feature          | Tuple  | List            |
| ---------------- | ------ | --------------- |
| Ordered          | ✅      | ✅               |
| Mutable          | ❌      | ✅               |
| Duplicate Values | ✅      | ✅               |
| Syntax           | `()`   | `[]`            |
| Performance      | Faster | Slightly Slower |

Use a **Tuple** when the data should never change.

Use a **List** when the data needs to be modified.

---

# 💡 When Should You Use Tuples?

Tuples are useful for:

* Coordinates
* RGB colors
* Dates
* Database records
* Configuration values
* Returning multiple values from a function

Example

```python
point = (120, 350)

rgb = (255, 0, 0)

date = (2026, 6, 30)
```

---

# ⚠ Common Mistakes

Trying to modify a tuple.

```python
numbers = (1, 2, 3)

numbers[0] = 10
```

❌ Output

```text
TypeError: 'tuple' object does not support item assignment
```

---

Forgetting the comma in a single-item tuple.

```python
value = (5)
```

Correct

```python
value = (5,)
```

---

# ✅ Best Practices

✔ Use tuples for fixed data.

✔ Use lists for changing data.

✔ Prefer tuple unpacking for cleaner code.

✔ Return multiple values from functions using tuples.


---

# 📚 Most Important Tuple Methods

| Method    | Description               |
| --------- | ------------------------- |
| `count()` | Count occurrences         |
| `index()` | Find the index of a value |

---

# 📝 Summary

* Tuples are ordered and immutable.
* They allow duplicate values.
* They support indexing and slicing.
* Tuples have only two built-in methods: `count()` and `index()`.
* Tuple unpacking is a powerful Python feature.
* Use tuples when data should remain unchanged.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide

---

## 📅 Last Updated

2026-06-30

---

## ⭐ Difficulty

🟢 Beginner

---

> 📖 Next Topic: Sets
