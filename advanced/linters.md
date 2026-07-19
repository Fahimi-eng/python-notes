# 📝 Linters in Python

> A linter analyzes your source code to detect syntax errors, style issues, unused code, and potential bugs before your program runs.

---

# 📚 What is a Linter?

A **linter** is a tool that automatically reviews your code and reports problems.

A linter helps you:

* Find programming mistakes
* Follow coding standards
* Improve code readability
* Reduce bugs
* Keep code consistent across a team

A linter **does not execute your program**. It only analyzes the source code.

---

# 🤔 Why Use a Linter?

Without a linter, problems might only appear when the program is executed.

Example

```python
def greet(name)
    print(f"Hello {name}")
```

A linter immediately reports the missing colon (`:`).

---

# 🔍 What Can a Linter Detect?

* Syntax errors
* Unused variables
* Unused imports
* Undefined variables
* Duplicate code (some linters)
* Bad formatting
* Missing whitespace
* Incorrect naming
* Complexity issues
* Possible bugs

---

# 📖 Linter vs Formatter

Many beginners confuse these two tools.

| Tool          | Purpose                        |
| ------------- | ------------------------------ |
| **Linter**    | Finds problems in the code     |
| **Formatter** | Automatically formats the code |

Example:

**Linter**

```python
x=10
print(y)
```

Reports:

* Missing whitespace
* Undefined variable `y`

Formatter changes it to:

```python
x = 10
print(y)
```

Notice that the formatter fixes the spacing, but it cannot fix the undefined variable.

---

# ⭐ Popular Python Linters

| Tool         | Description                                         |
| ------------ | --------------------------------------------------- |
| **Ruff**     | Extremely fast linter written in Rust (recommended) |
| **Pylint**   | Very detailed static code analysis                  |
| **Flake8**   | Popular and lightweight                             |
| **Pyflakes** | Finds common programming mistakes                   |
| **Mypy**     | Static type checker for type hints                  |

---

# 🚀 Installing Ruff

```bash
pip install ruff
```

Check a file

```bash
ruff check main.py
```

Check an entire project

```bash
ruff check .
```

Automatically fix supported issues

```bash
ruff check . --fix
```

---

# 🚀 Installing Pylint

```bash
pip install pylint
```

Run it

```bash
pylint main.py
```

---

# 🚀 Installing Flake8

```bash
pip install flake8
```

Run

```bash
flake8 .
```

---

# 📚 Example

Code

```python
import math

x=10

print(y)
```

A linter may report:

* `math` imported but unused
* Missing whitespace around `=`
* Undefined variable `y`

---

# ⭐ PEP 8

Most linters check your code against **PEP 8**, the official Python style guide.

Examples:

✔ Four spaces for indentation

✔ Meaningful variable names

✔ Maximum recommended line length

✔ Blank lines between functions

✔ Proper import order

---

# 🔧 Configuration

Many linters support configuration files.

Example

```text
pyproject.toml
```

or

```text
ruff.toml
```

Example

```toml
line-length = 100
```

---

# 💻 VS Code Integration

Install the following extensions:

* Python
* Ruff
* Pylance

Enable automatic linting.

Now errors appear while you type.

---

# 🔗 Ruff + Formatter

Ruff can also format code.

Format a project

```bash
ruff format .
```

Check code

```bash
ruff check .
```

Fix issues

```bash
ruff check . --fix
```

Many modern Python projects use Ruff for both linting and formatting.

---

# ⚠ Common Mistakes

### Ignoring linter warnings

Do not simply ignore warnings.

Understand why they appear and fix the root cause.

---

### Using multiple tools with conflicting rules

Choose a consistent toolchain.

Example:

* Ruff
* Black
* Mypy

or simply:

* Ruff (lint + format)

---

### Disabling too many rules

Avoid disabling warnings unless you understand the consequences.

---

# ✅ Best Practices

✔ Run the linter before every commit.

✔ Follow PEP 8.

✔ Remove unused imports.

✔ Remove unused variables.

✔ Write descriptive names.

✔ Keep functions short.

✔ Fix warnings instead of ignoring them.

---

# 🧪 Practice

1. Install Ruff.
2. Create a file with an unused variable.
3. Create an undefined variable.
4. Run `ruff check .`
5. Fix all reported issues.
6. Run `ruff check . --fix`.
7. Configure Ruff using `pyproject.toml`.

---

# 📚 Linter Cheat Sheet

| Command              | Description                        |
| -------------------- | ---------------------------------- |
| `ruff check .`       | Analyze the current project        |
| `ruff check . --fix` | Automatically fix supported issues |
| `ruff format .`      | Format the project                 |
| `pylint file.py`     | Analyze one file with Pylint       |
| `flake8 .`           | Run Flake8 on the project          |

---

# 📝 Summary

* A linter analyzes code without executing it.
* Linters detect syntax errors, style issues, and possible bugs.
* A formatter fixes code style automatically, while a linter reports problems.
* Ruff is currently one of the fastest and most popular Python tools because it supports both linting and formatting.
* Following PEP 8 makes code easier to read and maintain.

---

## 🔗 References

* Python Official Documentation
* PEP 8 – Style Guide for Python Code
* Ruff Documentation
* Pylint Documentation
* Flake8 Documentation

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟢 Beginner

