# 📝 Dictionaries in Python

> A dictionary is a mutable collection that stores data as **key-value pairs**.

---

# 📚 What is a Dictionary?

A **Dictionary** is one of Python's built-in data structures used to store related data.

Unlike lists, dictionaries do **not** use numeric indexes.

Instead, every value is associated with a unique **key**.

Example:

```python
student = {
    "name": "Alireza",
    "age": 24,
    "major": "Computer Engineering"
}
```

Here:

* `"name"` is a key.
* `"Alireza"` is its value.

---

# ✨ Characteristics of Dictionaries

Python dictionaries are:

* ✅ Mutable
* ✅ Store data as key-value pairs
* ✅ Keys must be unique
* ✅ Values can be duplicated
* ✅ Can store different data types
* ✅ Can contain nested dictionaries and lists

---

# 📌 Creating Dictionaries

### Empty Dictionary

```python
person = {}
```

or

```python
person = dict()
```

---

### Dictionary with Values

```python
person = {
    "name": "Alireza",
    "age": 24,
    "country": "Iran"
}
```

---

# 🎯 Accessing Values

Using square brackets

```python
print(person["name"])
```

Output

```text
Alireza
```

---

Using `get()`

```python
print(person.get("age"))
```

The `get()` method returns `None` instead of raising an error if the key doesn't exist.

```python
print(person.get("email"))
```

Output

```text
None
```

---

# ✏ Adding New Items

```python
person["email"] = "example@gmail.com"
```

---

# 🔄 Updating Values

```python
person["age"] = 25
```

---

# ❌ Removing Items

## pop()

```python
person.pop("country")
```

---

## popitem()

Removes the last inserted item.

```python
person.popitem()
```

---

## del

```python
del person["age"]
```

Delete the entire dictionary.

```python
del person
```

---

## clear()

Remove all items.

```python
person.clear()
```

---

# 🔍 Checking Keys

```python
if "name" in person:
    print("Key exists")
```

---

# 🔁 Loop Through a Dictionary

### Loop through keys

```python
for key in person:
    print(key)
```

---

### Loop through values

```python
for value in person.values():
    print(value)
```

---

### Loop through key-value pairs

```python
for key, value in person.items():
    print(key, value)
```

---

# 📏 Dictionary Length

```python
print(len(person))
```

---

# 📚 Useful Dictionary Methods

## keys()

Returns all keys.

```python
person.keys()
```

---

## values()

Returns all values.

```python
person.values()
```

---

## items()

Returns key-value pairs.

```python
person.items()
```

---

## update()

Updates multiple values.

```python
person.update({
    "age": 26,
    "country": "Germany"
})
```

---

## copy()

Creates a shallow copy.

```python
new_person = person.copy()
```

---

# 🪆 Nested Dictionaries

A dictionary can contain another dictionary.

```python
student = {
    "name": "Alireza",
    "address": {
        "city": "Birjand",
        "country": "Iran"
    }
}
```

Access nested values.

```python
print(student["address"]["city"])
```

Output

```text
Birjand
```

---

# 📋 Dictionary vs List

| Feature          | Dictionary | List     |
| ---------------- | ---------- | -------- |
| Access           | By Key     | By Index |
| Mutable          | ✅          | ✅        |
| Ordered          | ✅          | ✅        |
| Duplicate Keys   | ❌          | —        |
| Duplicate Values | ✅          | ✅        |

Use a **Dictionary** when your data has labels.

Use a **List** when the order of items is the most important thing.

---

# 💡 When Should You Use Dictionaries?

Use dictionaries when storing:

* User information
* Product details
* API responses
* Configuration settings
* JSON data
* Database records

Example

```python
user = {
    "id": 1,
    "username": "alireza",
    "email": "example@gmail.com",
    "is_admin": False
}
```

---

# ⚠ Common Mistakes

Trying to access a missing key.

```python
print(person["phone"])
```

❌ Output

```text
KeyError
```

Better

```python
print(person.get("phone"))
```

---

Using duplicate keys.

```python
person = {
    "name": "Ali",
    "name": "Sara"
}
```

Output

```python
{'name': 'Sara'}
```

The last value overwrites the previous one.

---

# ✅ Best Practices

✔ Use meaningful key names.

✔ Prefer `get()` when a key might not exist.

✔ Use `items()` when you need both keys and values.

✔ Keep keys consistent (usually strings).

✔ Use nested dictionaries for structured data.

---

# 📚 Most Important Dictionary Methods

| Method      | Description            |
| ----------- | ---------------------- |
| `get()`     | Get a value safely     |
| `keys()`    | Return all keys        |
| `values()`  | Return all values      |
| `items()`   | Return key-value pairs |
| `update()`  | Update multiple values |
| `pop()`     | Remove a key           |
| `popitem()` | Remove the last item   |
| `clear()`   | Remove all items       |
| `copy()`    | Copy the dictionary    |

---

# 📝 Summary

* Dictionaries store data as key-value pairs.
* Keys must be unique.
* Values can be duplicated.
* Dictionaries are mutable.
* Access values using keys.
* Use `get()` to safely retrieve values.
* Dictionaries are ideal for structured and labeled data.

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

> 📖 Next Topic: tuples
