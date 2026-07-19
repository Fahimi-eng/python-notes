# 📝 Exception Handling in Python

> Exception handling allows Python programs to detect, handle, and recover from runtime errors without crashing.

---

# 📚 What is an Exception?

An **exception** is an error that occurs while a program is running.

If an exception is not handled, Python stops the program and displays an error message.

Example

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError: division by zero
```

---

# 🤔 Why Use Exception Handling?

Exception handling helps you:

* ✅ Prevent program crashes
* ✅ Display user-friendly error messages
* ✅ Recover from expected errors
* ✅ Keep applications stable
* ✅ Separate normal logic from error-handling logic

---

# 🔹 The `try` Block

Place code that may raise an exception inside a `try` block.

```python
try:
    number = 10 / 0
```

---

# 🔹 The `except` Block

Handle an exception when it occurs.

```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Output

```text
You cannot divide by zero.
```

---

# 🔹 Catching Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# 🔹 Catching Multiple Exception Types

```python
try:
    value = int(input("Enter a number: "))
except (ValueError, TypeError):
    print("Invalid input.")
```

---

# 🔹 The `else` Block

The `else` block runs only if no exception occurs.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered:", number)
```

---

# 🔹 The `finally` Block

The `finally` block always executes, whether an exception occurs or not.

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finished.")
```

A common use case is closing files or releasing resources.

---

# 🔹 Complete Example

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter an integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
```

---

# 🔹 Raising Exceptions

Use `raise` to create your own exceptions.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# 🔹 Re-raising Exceptions

Sometimes you need to perform additional work before passing the exception upward.

```python
try:
    value = int("abc")
except ValueError:
    print("Logging the error...")
    raise
```

---

# 🔹 Custom Exceptions

Create your own exception class.

```python
class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    pass
```

Use it

```python
age = -1

if age < 0:
    raise InvalidAgeError("Age must be zero or greater.")
```

---

# 🔹 Common Built-in Exceptions

| Exception             | Description             |
| --------------------- | ----------------------- |
| `ValueError`          | Invalid value           |
| `TypeError`           | Wrong data type         |
| `IndexError`          | Invalid list index      |
| `KeyError`            | Missing dictionary key  |
| `NameError`           | Undefined variable      |
| `AttributeError`      | Object has no attribute |
| `FileNotFoundError`   | File does not exist     |
| `ZeroDivisionError`   | Division by zero        |
| `ImportError`         | Import failed           |
| `ModuleNotFoundError` | Module not found        |

---

# 💡 Real-World Examples

### Reading a File Safely

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")
```

---

### Safe Dictionary Access

```python
user = {
    "name": "Ali"
}

try:
    print(user["age"])

except KeyError:
    print("Age was not found.")
```

---

### Safe User Input

```python
while True:
    try:
        age = int(input("Enter your age: "))
        break

    except ValueError:
        print("Please enter a valid number.")
```

---

# ⚠ Common Mistakes

### Catching every exception

Avoid

```python
try:
    do_something()

except:
    print("Something went wrong.")
```

Prefer

```python
try:
    do_something()

except ValueError:
    print("Invalid value.")
```

Catching specific exceptions makes debugging much easier.

---

### Ignoring exceptions

Avoid

```python
try:
    do_something()

except Exception:
    pass
```

This hides errors and makes problems difficult to find.

---

### Using exceptions instead of validation

Wrong

```python
try:
    age = int(user_input)
except:
    age = 0
```

Prefer validating input where possible and only using exceptions for exceptional situations.

---

# ✅ Best Practices

✔ Catch specific exceptions instead of using a bare `except`.

✔ Keep `try` blocks as small as possible.

✔ Use `finally` to release resources.

✔ Use `with` for file handling.

✔ Raise meaningful exceptions when needed.

✔ Create custom exceptions for business logic.

✔ Never silently ignore unexpected exceptions.

---

# 🧪 Practice

1. Handle a `ZeroDivisionError`.
2. Handle invalid user input (`ValueError`).
3. Read a file safely using `try` and `except`.
4. Use `else` after a successful operation.
5. Use `finally` to print a completion message.
6. Raise a custom `ValueError` if a number is negative.
7. Create a custom exception class called `InvalidPasswordError`.

---

# 📚 Exception Handling Cheat Sheet

| Keyword     | Description                    |
| ----------- | ------------------------------ |
| `try`       | Wrap code that may fail        |
| `except`    | Handle an exception            |
| `else`      | Execute if no exception occurs |
| `finally`   | Always execute                 |
| `raise`     | Raise an exception             |
| `Exception` | Base class for most exceptions |

---

# 📝 Summary

* Exceptions are runtime errors.
* Use `try` and `except` to prevent crashes.
* `else` runs only if no exception occurs.
* `finally` always executes and is useful for cleanup.
* Use `raise` to create your own exceptions.
* Prefer handling specific exception types.
* Write clear, informative error messages.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide
* Effective Python by Brett Slatkin

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟡 Intermediate

---

> 📖 Next Topic: Iterators & Generators
