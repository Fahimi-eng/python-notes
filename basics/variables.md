# 📝 Variables in Python

> Variables are used to store data in memory.

---

# 📚 What is a Variable?

A **variable** is a name that refers to a value stored in memory.

Think of it as a labeled box that stores information.

```python
name = "Alice"
age = 22
```

Here:

* `name` is a variable.
* `"Alice"` is the value.
* `=` is the assignment operator.

---

# 🧠 Variable Assignment

```python
language = "Python"
version = 3.13
```

Python creates variables automatically when you assign a value.

Unlike some programming languages, you **don't need to declare the type**.

---

# 📦 Multiple Assignments

## Assign multiple values

```python
x, y, z = 10, 20, 30
```

---

## Assign one value to multiple variables

```python
a = b = c = 100
```

---

# 🔄 Reassigning Variables

Variables can change during program execution.

```python
score = 50

score = 75

score = 100
```

The latest value replaces the previous one.

---

# 🏷 Naming Rules

A variable name:

✅ Can contain letters

```python
username
```

✅ Can contain numbers (not at the beginning)

```python
user1
```

✅ Can contain underscores

```python
first_name
```

---

Cannot:

```python
1name
```

```python
first-name
```

```python
my name
```

---

# ✅ Naming Convention (PEP 8)

Use **snake_case**

```python
first_name
total_price
student_age
```

Avoid:

```python
FirstName
TOTALPRICE
myVariable
```

---

# 📋 Reserved Keywords

These names cannot be used as variables.

```python
if
for
while
class
return
import
True
False
None
```

Example:

```python
# ❌ Invalid

class = "Python"
```

---

# 🔍 Checking Variable Type

```python
age = 20

print(type(age))
```

Output

```python
<class 'int'>
```

---

# 💡 Dynamic Typing

Python is dynamically typed.

```python
x = 10

x = "Hello"

x = 3.14
```

The variable can reference different data types.

---

# 🧪 Examples

```python
name = "John"
age = 25
height = 1.82
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

---

# ⚠ Common Mistakes

❌ Using spaces

```python
my name = "Ali"
```

---

❌ Starting with a number

```python
2value = 50
```

---

❌ Using reserved keywords

```python
for = 10
```

---

# ✅ Best Practices

✔ Use meaningful names.

```python
user_age
```

instead of

```python
a
```

---

✔ Keep names short but descriptive.

Good

```python
total_price
```

Bad

```python
tp
```

---

✔ Follow PEP 8 naming conventions.

---

# 🧩 Practice

Create the following variables:

* Your name
* Your age
* Your country
* Your favorite programming language
* Whether you are a student (`True` or `False`)

Example:

```python
name = "Alireza"
age = 24
country = "Iran"
language = "Python"
is_student = False
```

---

# 📌 Summary

* Variables store data.
* Python creates variables automatically.
* No type declaration is needed.
* Variables can change their values.
* Use meaningful snake_case names.
* Avoid reserved keywords.
* Follow PEP 8.

---

> 📖 Next Topic: Data Types
