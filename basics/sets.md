# 📝 Sets in Python

> A set is an unordered, mutable collection of unique items.

---

# 📚 What is a Set?

A **Set** is one of Python's built-in data structures used to store **unique values**.

Unlike lists and tuples, sets automatically remove duplicate items.

Example:

```python
numbers = {1, 2, 3, 4}
```

If duplicate values exist:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output

```python
{1, 2, 3, 4}
```

---

# ✨ Characteristics of Sets

Python sets are:

* ✅ Unordered
* ✅ Mutable
* ✅ Do NOT allow duplicate values
* ✅ Can store different immutable data types
* ✅ Very fast for membership testing (`in`)
* ❌ Do not support indexing or slicing

---

# 📌 Creating Sets

### Empty Set

```python
items = set()
```

⚠️ Do **not** use `{}` because it creates an empty dictionary.

---

### Set with Values

```python
languages = {"Python", "Java", "Go"}
```

---

### Creating a Set from a List

```python
numbers = set([1, 2, 2, 3, 4])
```

Output

```python
{1, 2, 3, 4}
```

---

# ➕ Adding Items

## add()

Adds one item.

```python
languages.add("Rust")
```

---

## update()

Adds multiple items.

```python
languages.update({"C#", "PHP"})
```

or

```python
languages.update(["JavaScript", "Swift"])
```

---

# ❌ Removing Items

## remove()

Removes an item.

```python
languages.remove("Java")
```

⚠️ Raises an error if the item does not exist.

---

## discard()

```python
languages.discard("Java")
```

Unlike `remove()`, no error is raised if the item is missing.

---

## pop()

Removes and returns a random item.

```python
languages.pop()
```

Because sets are unordered, you cannot predict which item will be removed.

---

## clear()

Remove all items.

```python
languages.clear()
```

---

# 🔍 Checking Membership

```python
"Python" in languages
```

Output

```python
True
```

Membership testing in sets is much faster than in lists.

---

# 🔁 Loop Through a Set

```python
for language in languages:
    print(language)
```

⚠️ The order is not guaranteed.

---

# 📏 Length

```python
len(languages)
```

---

# 📚 Set Operations

## Union

Combine two sets.

```python
set1 = {1, 2, 3}

set2 = {3, 4, 5}

print(set1 | set2)
```

or

```python
print(set1.union(set2))
```

Output

```python
{1, 2, 3, 4, 5}
```

---

## Intersection

Common values.

```python
print(set1 & set2)
```

or

```python
print(set1.intersection(set2))
```

Output

```python
{3}
```

---

## Difference

Values only in the first set.

```python
print(set1 - set2)
```

or

```python
print(set1.difference(set2))
```

Output

```python
{1, 2}
```

---

## Symmetric Difference

Values that exist in only one set.

```python
print(set1 ^ set2)
```

or

```python
print(set1.symmetric_difference(set2))
```

Output

```python
{1, 2, 4, 5}
```

---

# 📋 Useful Set Methods

## copy()

```python
new_set = languages.copy()
```

---

## issubset()

Checks whether a set is a subset of another.

```python
a = {1, 2}

b = {1, 2, 3}

a.issubset(b)
```

---

## issuperset()

Checks whether a set contains another set.

```python
b.issuperset(a)
```

---

## isdisjoint()

Checks whether two sets have no common elements.

```python
a.isdisjoint({5, 6})
```

---

# 📋 Set vs List

| Feature          | Set    | List   |
| ---------------- | ------ | ------ |
| Ordered          | ❌      | ✅      |
| Mutable          | ✅      | ✅      |
| Duplicate Values | ❌      | ✅      |
| Indexing         | ❌      | ✅      |
| Membership Test  | ⭐ Fast | Slower |

Use a **Set** when uniqueness and fast lookups are important.

Use a **List** when order matters.

---

# 💡 When Should You Use Sets?

Sets are useful for:

* Removing duplicate values
* Comparing collections
* Fast membership testing
* Finding common items
* Data analysis
* Mathematical set operations

Example

```python
emails = [
    "a@test.com",
    "b@test.com",
    "a@test.com"
]

unique_emails = set(emails)
```

Output

```python
{"a@test.com", "b@test.com"}
```

---

# ⚠ Common Mistakes

Trying to access an item by index.

```python
numbers = {1, 2, 3}

print(numbers[0])
```

❌ Output

```text
TypeError: 'set' object is not subscriptable
```

---

Creating an empty set incorrectly.

```python
items = {}
```

This creates a dictionary.

Correct

```python
items = set()
```

---

# ✅ Best Practices

✔ Use sets to remove duplicates.

✔ Use sets for fast membership testing.

✔ Use `discard()` if the item may not exist.

✔ Use set operations instead of manual loops whenever possible.

---

# 📚 Most Important Set Methods

| Method                   | Description               |
| ------------------------ | ------------------------- |
| `add()`                  | Add one item              |
| `update()`               | Add multiple items        |
| `remove()`               | Remove an item            |
| `discard()`              | Remove safely             |
| `pop()`                  | Remove a random item      |
| `clear()`                | Remove all items          |
| `copy()`                 | Copy the set              |
| `union()`                | Combine sets              |
| `intersection()`         | Common items              |
| `difference()`           | Difference between sets   |
| `symmetric_difference()` | Items unique to each set  |
| `issubset()`             | Check subset              |
| `issuperset()`           | Check superset            |
| `isdisjoint()`           | Check for no common items |

---

# 📝 Summary

* Sets store unique values.
* Sets are unordered and mutable.
* Duplicate values are removed automatically.
* Sets are excellent for fast membership checks.
* They support powerful mathematical operations such as union, intersection, and difference.
* Sets do not support indexing or slicing.

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

