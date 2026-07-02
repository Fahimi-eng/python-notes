# 📝 File I/O in Python

> File I/O (Input/Output) allows Python programs to read data from files and write data to files.

---

# 📚 What is File I/O?

File I/O stands for **File Input/Output**.

It enables your program to:

* 📖 Read data from files
* ✍ Write data to files
* ➕ Append new data
* 📂 Create new files
* 🗑 Update existing files

Without File I/O, all data would be lost when the program exits.

---

# 📌 Opening a File

Use the built-in `open()` function.

```python
file = open("example.txt", "r")
```

Syntax

```python
open(file_path, mode)
```

---

# 📚 File Modes

| Mode   | Description                                    |
| ------ | ---------------------------------------------- |
| `"r"`  | Read (default)                                 |
| `"w"`  | Write (overwrite if exists)                    |
| `"a"`  | Append to the end of a file                    |
| `"x"`  | Create a new file (fails if it already exists) |
| `"rb"` | Read binary files                              |
| `"wb"` | Write binary files                             |

---

# ⭐ Using `with` (Recommended)

The safest way to work with files is by using a **Context Manager**.

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Advantages:

* Automatically closes the file.
* Cleaner code.
* Prevents resource leaks.
* Recommended by Python developers.

---

# 📖 Reading Files

## Read the entire file

```python
with open("example.txt", "r") as file:
    content = file.read()

print(content)
```

---

## Read one line

```python
with open("example.txt", "r") as file:
    line = file.readline()

print(line)
```

---

## Read all lines

```python
with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Output

```python
['First line\n', 'Second line\n']
```

---

## Read line by line

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This approach is memory-efficient for large files.

---

# ✍ Writing Files

Writing replaces the file content.

```python
with open("example.txt", "w") as file:
    file.write("Hello Python!")
```

If the file does not exist, Python creates it.

---

# ➕ Appending to a File

Append new data without removing existing content.

```python
with open("example.txt", "a") as file:
    file.write("\nNew line")
```

---

# 🆕 Creating a New File

```python
with open("new_file.txt", "x") as file:
    file.write("New file created.")
```

Raises an error if the file already exists.

---

# 📂 Working with File Paths

Relative path

```python
with open("data/users.txt")
```

Absolute path

```python
with open("C:/Users/Alireza/Documents/users.txt")
```

---

# 🔒 Closing Files

Without `with`

```python
file = open("example.txt", "r")

print(file.read())

file.close()
```

Using `with`, closing happens automatically.

---

# ⚠ Handling Errors

Trying to open a file that doesn't exist raises an exception.

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

# 📏 Checking File Information

```python
with open("example.txt", "r") as file:
    print(file.name)
    print(file.mode)
    print(file.closed)
```

---

# 📋 Common File Methods

| Method         | Description                |
| -------------- | -------------------------- |
| `read()`       | Read the entire file       |
| `readline()`   | Read one line              |
| `readlines()`  | Read all lines into a list |
| `write()`      | Write text                 |
| `writelines()` | Write multiple lines       |
| `close()`      | Close the file             |

---

# 💡 Best Practices

✔ Always use `with open()`.

✔ Handle possible exceptions.

✔ Use UTF-8 encoding when working with text.

```python
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

✔ Read large files line by line instead of using `read()`.

✔ Choose the correct file mode.

---

# ⚠ Common Mistakes

Opening a file without closing it.

```python
file = open("example.txt")
```

Better

```python
with open("example.txt") as file:
    print(file.read())
```

---

Using `"w"` when you meant to append.

```python
with open("example.txt", "w") as file:
    file.write("Hello")
```

This overwrites the existing file.

Use `"a"` if you want to keep the existing content.

---

# 🧪 Practice

Create a file named `notes.txt`.

1. Write three lines into the file.
2. Read the entire file.
3. Print each line separately.
4. Append a new line.
5. Read the updated content.

Example:

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Git\n")
    file.write("GitHub\n")
```

---

# 📚 File Modes Cheat Sheet

| Mode | Read | Write | Create | Overwrite           |
| ---- | ---- | ----- | ------ | ------------------- |
| `r`  | ✅    | ❌     | ❌      | ❌                   |
| `w`  | ❌    | ✅     | ✅      | ✅                   |
| `a`  | ❌    | ✅     | ✅      | ❌                   |
| `x`  | ❌    | ✅     | ✅      | ❌ (Fails if exists) |

---

# 📝 Summary

* File I/O allows programs to read and write files.
* Use `open()` to work with files.
* Prefer `with open()` because it closes files automatically.
* Use the appropriate file mode (`r`, `w`, `a`, `x`).
* Handle file-related exceptions.
* Use UTF-8 encoding for text files whenever possible.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟡 Intermediate


