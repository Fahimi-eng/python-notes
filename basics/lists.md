# 📝 Lists in Python

> A list is an ordered, mutable collection that can store multiple items of different data types.

---

# 📚 What is a List?

A **list** is one of Python's most commonly used data structures.

Lists are:

* ✅ Ordered
* ✅ Mutable (can be changed)
* ✅ Allow duplicate values
* ✅ Can store different data types

Example:

```python
numbers = [10, 20, 30]
```

Lists can contain mixed data types.

```python
data = ["Python", 24, True, 3.14]
```

---

# 📌 Creating Lists

```python
languages = ["Python", "Java", "C++"]
```

Empty list

```python
items = []
```

Using the constructor

```python
numbers = list((1, 2, 3))
```

---

# 🎯 Accessing Items

First item

```python
languages[0]
```

Second item

```python
languages[1]
```

Last item

```python
languages[-1]
```

---

# ✂ Slicing

```python
numbers = [10, 20, 30, 40, 50]
```

First three items

```python
numbers[:3]
```

Last two items

```python
numbers[-2:]
```

Middle items

```python
numbers[1:4]
```

---

# ✏ Modify Items

```python
languages[1] = "Go"
```

Result

```python
["Python", "Go", "C++"]
```

---

# ➕ Add Items

## append()

Adds one item to the end.

```python
languages.append("Rust")
```

---

## extend()

Adds multiple items.

```python
languages.extend(["PHP", "JavaScript"])
```

---

## insert()

Insert at a specific position.

```python
languages.insert(1, "C#")
```

---

# ❌ Remove Items

## remove()

Removes the first matching value.

```python
languages.remove("Java")
```

---

## pop()

Remove by index.

```python
languages.pop(2)
```

Remove the last item.

```python
languages.pop()
```

---

## del

```python
del languages[0]
```

Delete the entire list.

```python
del languages
```

---

## clear()

Remove all items.

```python
languages.clear()
```

---

# 🔍 Search

## in

```python
if "Python" in languages:
    print("Found")
```

---

## index()

```python
languages.index("Python")
```

---

## count()

```python
numbers = [1, 2, 2, 3, 2]

numbers.count(2)
```

Output

```text
3
```

---

# 🔄 Sorting

## sort()

```python
numbers = [5, 2, 8, 1]

numbers.sort()
```

Descending

```python
numbers.sort(reverse=True)
```

---

## sorted()

Returns a new sorted list.

```python
new_numbers = sorted(numbers)
```

---

# 🔁 Reverse

```python
numbers.reverse()
```

---

# 📏 Length

```python
len(numbers)
```

---

# ➕ Concatenate Lists

```python
list1 = [1, 2]

list2 = [3, 4]

result = list1 + list2
```

---

# 🔂 Repeat Lists

```python
zeros = [0] * 5
```

Output

```python
[0, 0, 0, 0, 0]
```

---

# 📋 Copy Lists

## copy()

```python
new_list = numbers.copy()
```

---

## list()

```python
new_list = list(numbers)
```

---

## Slicing

```python
new_list = numbers[:]
```

---

# 🔁 Loop Through a List

```python
for language in languages:
    print(language)
```

---

Using index

```python
for index, language in enumerate(languages):
    print(index, language)
```

---

# ⚠ Common Mistakes

Trying to access an index that doesn't exist.

```python
numbers = [1, 2, 3]

print(numbers[10])
```

❌ IndexError

---

Confusing `append()` and `extend()`

```python
numbers.append([4, 5])
```

Result

```python
[1, 2, 3, [4, 5]]
```

Instead

```python
numbers.extend([4, 5])
```

Result

```python
[1, 2, 3, 4, 5]
```

---

# ✅ Best Practices

✔ Use `append()` for a single item.

✔ Use `extend()` for multiple items.

✔ Use `sorted()` when you don't want to modify the original list.

✔ Use `in` before searching for an item.

✔ Prefer `enumerate()` when both index and value are needed.


---

# 📚 Most Important List Methods

| Method      | Description                |
| ----------- | -------------------------- |
| `append()`  | Add one item               |
| `extend()`  | Add multiple items         |
| `insert()`  | Insert at a specific index |
| `remove()`  | Remove by value            |
| `pop()`     | Remove by index            |
| `clear()`   | Remove all items           |
| `index()`   | Find index                 |
| `count()`   | Count occurrences          |
| `sort()`    | Sort the list              |
| `reverse()` | Reverse the list           |
| `copy()`    | Copy the list              |

---

# 📝 Summary

* Lists are ordered and mutable.
* Lists can contain duplicate values.
* Items can be added, removed, and modified.
* Lists support indexing and slicing.
* `append()`, `extend()`, `remove()`, `pop()`, and `sort()` are the most frequently used methods.

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

> 📖 Next Topic: Tuples
