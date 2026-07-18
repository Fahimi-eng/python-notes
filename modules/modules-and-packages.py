# 📝 Modules & Packages in Python

> Modules and packages help organize Python code into reusable, maintainable, and scalable components.

---

# 📚 What is a Module?

A **module** is a single Python file (`.py`) that contains variables, functions, classes, or executable code.

Modules allow you to organize related code into separate files and reuse it across different projects.

Example:

```text
math_utils.py
```

```python
def add(a, b):
    return a + b

PI = 3.14159
```

---

# 📥 Importing a Module

Import the entire module.

```python
import math_utils

print(math_utils.add(10, 20))
```

---

Import a specific function.

```python
from math_utils import add

print(add(5, 3))
```

---

Import multiple items.

```python
from math_utils import add, PI
```

---

Import with an alias.

```python
import math_utils as mu

print(mu.add(1, 2))
```

---

# 📦 Built-in Modules

Python comes with many built-in modules.

Examples:

| Module     | Purpose                     |
| ---------- | --------------------------- |
| `math`     | Mathematical functions      |
| `random`   | Random values               |
| `datetime` | Date and time               |
| `os`       | Operating system operations |
| `sys`      | Python runtime information  |
| `pathlib`  | Modern file paths           |
| `json`     | JSON handling               |
| `csv`      | CSV files                   |
| `re`       | Regular expressions         |

Example

```python
import math

print(math.sqrt(25))
```

Output

```text
5.0
```

---

# 📁 What is a Package?

A **package** is a directory that contains one or more Python modules.

Packages help organize larger applications.

Example:

```text
my_project/
│
├── app/
│   ├── __init__.py
│   ├── users.py
│   ├── products.py
│   └── orders.py
│
└── main.py
```

---

# 📌 The `__init__.py` File

The `__init__.py` file tells Python that a directory should be treated as a package.

Example:

```text
app/
│
├── __init__.py
├── users.py
└── products.py
```

The file can be empty or contain initialization code.

---

# 📥 Importing from a Package

```python
from app.users import create_user
```

Import the entire module.

```python
import app.users
```

---

# ⭐ Absolute Imports

```python
from app.products import Product
```

Absolute imports are recommended because they are easier to read and maintain.

---

# ⭐ Relative Imports

```python
from .users import create_user
```

```python
from ..database import connection
```

Relative imports are mainly used inside packages.

---

# 📚 The `__name__` Variable

Every Python module has a special variable called `__name__`.

Example:

```python
print(__name__)
```

If the file is executed directly:

```text
__main__
```

If it is imported:

```text
module_name
```

---

# ⭐ The `if __name__ == "__main__"` Pattern

This allows code to run only when the file is executed directly.

```python
def hello():
    print("Hello")

if __name__ == "__main__":
    hello()
```

This is commonly used for testing modules.

---

# 📥 Installing Third-Party Packages

Use `pip`.

```bash
pip install requests
```

Upgrade a package.

```bash
pip install --upgrade requests
```

Remove a package.

```bash
pip uninstall requests
```

List installed packages.

```bash
pip list
```

---

# 📄 Requirements File

Save project dependencies.

Create:

```text
requirements.txt
```

Generate automatically.

```bash
pip freeze > requirements.txt
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🌐 Virtual Environments

Use virtual environments to isolate project dependencies.

Create

```bash
python -m venv .venv
```

Activate

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Deactivate

```bash
deactivate
```

---

# 📚 Useful Standard Library Modules

## `math`

```python
import math

print(math.pi)
print(math.sqrt(16))
```

---

## `random`

```python
import random

print(random.randint(1, 10))
```

---

## `datetime`

```python
from datetime import datetime

print(datetime.now())
```

---

## `os`

```python
import os

print(os.getcwd())
```

---

## `pathlib`

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
```

---

# ⚠ Common Mistakes

### Naming a file after a standard library module

Wrong

```text
random.py
```

Then

```python
import random
```

Python imports your file instead of the standard library module.

---

### Using wildcard imports

Avoid

```python
from math import *
```

Prefer

```python
from math import sqrt
```

or

```python
import math
```

---

### Forgetting to activate the virtual environment

Always activate the correct environment before installing packages.

---

# 💡 Best Practices

✔ Use one module for one responsibility.

✔ Group related modules into packages.

✔ Prefer absolute imports.

✔ Avoid wildcard imports.

✔ Always use a virtual environment.

✔ Keep dependencies in `requirements.txt`.

✔ Follow PEP 8 naming conventions.

---

# 🧪 Practice

Create the following structure:

```text
calculator/
│
├── __init__.py
├── math_utils.py
├── string_utils.py
└── main.py
```

Tasks:

1. Create an `add()` function in `math_utils.py`.
2. Create a `capitalize_name()` function in `string_utils.py`.
3. Import both functions into `main.py`.
4. Create a virtual environment.
5. Install the `requests` package.
6. Generate a `requirements.txt` file.

---

# 📚 Import Cheat Sheet

| Statement                         | Description            |
| --------------------------------- | ---------------------- |
| `import module`                   | Import a module        |
| `import module as alias`          | Import with an alias   |
| `from module import name`         | Import a specific item |
| `from package.module import name` | Import from a package  |
| `from .module import name`        | Relative import        |

---

# 📝 Summary

* A **module** is a single Python file.
* A **package** is a directory containing related modules.
* Use `import` to reuse code from other modules.
* The `__init__.py` file identifies a package.
* Prefer absolute imports over relative imports when possible.
* Use `if __name__ == "__main__"` to separate reusable code from executable code.
* Manage third-party libraries with `pip`.
* Use virtual environments for project isolation.
* Record dependencies in `requirements.txt`.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide
* Python Packaging User Guide

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🟡 Intermediate

---

> 📖 Next Topic: Exception Handling
