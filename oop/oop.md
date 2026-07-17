# 📝 Object-Oriented Programming (OOP) in Python

> Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes, making applications more modular, reusable, and easier to maintain.

---

# 📚 What is OOP?

Object-Oriented Programming (OOP) is a way of writing programs by modeling real-world entities as **objects**.

An object contains:

* **Attributes** (Data)
* **Methods** (Behavior)

Example:

A `Car` object might have:

Attributes

* Brand
* Model
* Color
* Speed

Methods

* Start
* Stop
* Accelerate

---

# 💡 Why Use OOP?

OOP helps developers build software that is:

* ✅ Reusable
* ✅ Easy to maintain
* ✅ Scalable
* ✅ Organized
* ✅ Easy to test

Most modern Python frameworks make heavy use of OOP.

---

# 📖 Class vs Object

## Class

A class is a blueprint for creating objects.

Example

```python
class Car:
    pass
```

---

## Object

An object is an instance of a class.

```python
car = Car()
```

---

# 🔹 Creating a Class

```python
class Person:
    pass
```

Create an object

```python
person = Person()
```

---

# 🔹 The `__init__()` Constructor

The constructor initializes an object.

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create an object

```python
person = Person("Alireza", 24)
```

---

# 🔹 The `self` Keyword

`self` refers to the current object.

```python
class Person:

    def __init__(self, name):
        self.name = name
```

Every instance has its own value.

---

# 🔹 Instance Attributes

```python
class Person:

    def __init__(self, name):
        self.name = name
```

Access

```python
print(person.name)
```

---

# 🔹 Instance Methods

```python
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")
```

Call

```python
person.greet()
```

---

# 🔹 Class Attributes

Shared between all objects.

```python
class Person:

    species = "Human"
```

Access

```python
print(Person.species)
```

---

# 🔹 Encapsulation

Hide internal data and control access.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

Private attribute

```python
account = BankAccount(1000)
```

Cannot access

```python
account.__balance
```

---

# 🔹 Getter and Setter

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount
```

---

# 🔹 Inheritance

A class can inherit from another class.

```python
class Animal:

    def speak(self):
        print("Animal sound")
```

Child class

```python
class Dog(Animal):

    def bark(self):
        print("Woof")
```

---

# 🔹 Method Overriding

Child classes can replace parent methods.

```python
class Animal:

    def speak(self):
        print("Animal")
```

```python
class Dog(Animal):

    def speak(self):
        print("Woof")
```

---

# 🔹 Polymorphism

Different objects can respond differently to the same method.

```python
animals = [Dog(), Animal()]

for animal in animals:
    animal.speak()
```

---

# 🔹 Abstraction

Hide implementation details.

```python
from abc import ABC, abstractmethod
```

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

---

# 🔹 Magic Methods

Special methods surrounded by double underscores.

Examples

```python
__init__()

__str__()

__repr__()

__len__()

__eq__()
```

Example

```python
class Person:

    def __str__(self):
        return "Person Object"
```

---

# 🔹 Static Methods

Methods that do not use object data.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Call

```python
Math.add(2, 3)
```

---

# 🔹 Class Methods

Operate on the class instead of an instance.

```python
class Person:

    count = 0

    @classmethod
    def total(cls):
        return cls.count
```

---

# 🔹 Property Decorator

Use methods like attributes.

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2
```

---

# 📚 The Four Pillars of OOP

| Principle     | Description                        |
| ------------- | ---------------------------------- |
| Encapsulation | Hide data                          |
| Inheritance   | Reuse code                         |
| Polymorphism  | Same interface, different behavior |
| Abstraction   | Hide implementation                |

---

# 💡 Real-World Example

```python
class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passed(self):
        return self.grade >= 50
```

Usage

```python
student = Student("Sara", 90)

print(student.is_passed())
```

Output

```text
True
```

---

# ⚠ Common Mistakes

Forgetting `self`

Wrong

```python
class Person:

    def greet():
        print("Hello")
```

Correct

```python
class Person:

    def greet(self):
        print("Hello")
```

---

Creating unnecessary classes.

Not every piece of code needs OOP.

---

# ✅ Best Practices

✔ Use meaningful class names.

✔ Keep classes focused on one responsibility.

✔ Prefer composition over deep inheritance.

✔ Keep attributes private when appropriate.

✔ Use properties instead of exposing internal state directly.

✔ Write small, reusable methods.

---

# 🧪 Practice

Create the following classes:

1. `Person`
2. `Student`
3. `Car`
4. `Rectangle`
5. `BankAccount`
6. `Employee`
7. `Animal` and `Dog`
8. `Shape` (Abstract Class)
9. `Book`

Implement constructors, attributes, and useful methods for each.

---

# 📚 OOP Cheat Sheet

| Concept            | Purpose                         |
| ------------------ | ------------------------------- |
| `class`            | Define a class                  |
| Object             | Instance of a class             |
| `__init__()`       | Constructor                     |
| `self`             | Current object                  |
| Instance Attribute | Data unique to each object      |
| Class Attribute    | Shared data                     |
| Inheritance        | Extend another class            |
| Polymorphism       | Same method, different behavior |
| Encapsulation      | Protect data                    |
| Abstraction        | Hide implementation             |
| `@staticmethod`    | Utility method                  |
| `@classmethod`     | Class-level method              |
| `@property`        | Computed attribute              |

---

# 📝 Summary

* OOP organizes programs around classes and objects.
* A class is a blueprint, and an object is an instance of that blueprint.
* Constructors initialize object data.
* Encapsulation protects internal state.
* Inheritance enables code reuse.
* Polymorphism allows different objects to share a common interface.
* Abstraction simplifies complex systems.
* Python provides decorators like `@staticmethod`, `@classmethod`, and `@property` for advanced object-oriented programming.

---

## 🔗 References

* Python Official Documentation
* PEP 8 Style Guide
* Fluent Python by Luciano Ramalho

---

## 📅 Last Updated

2026-07-02

---

## ⭐ Difficulty

🔴 Advanced

---

> 📖 Next Topic: Modules & Packages
