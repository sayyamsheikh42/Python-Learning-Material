# 🐍 Advanced Python Functions & Patterns

> **Transform from Python user to Python power user!**  
> Master 9 essential advanced concepts that make your code cleaner, faster, and more reusable.

## 📚 Table of Contents

1. [🎯 Closures](#-closures)
2. [🎁 Function Decorators](#-function-decorators)
3. [🏗️ Class Decorators](#️-class-decorators)
4. [🔄 Higher-Order Functions](#-higher-order-functions)
5. [✨ Advanced Comprehensions](#-advanced-comprehensions)
6. [🔧 Partial Functions](#-partial-functions)
7. [⚡ Caching (lru_cache)](#-caching-lru_cache)
8. [🔄 Advanced Iterators & Generators](#-advanced-iterators--generators)
9. [🛡️ Context Managers](#️-context-managers)

---

## 🎯 Closures

**What is it?** A function that "remembers" variables from where it was created, even after that scope is gone.

### 🧠 Mental Model
```python
def outer():
    x = 10        # ← This gets "captured"
    def inner():  # ← This is the closure
        return x  # ← It remembers x!
    return inner

my_func = outer()  # outer() is done, but...
print(my_func())   # inner() still remembers x = 10!
```

### 🎯 Why Use Closures?
- **Keep state** without classes (like counters, timers)
- **Create configurable functions** (validators, formatters)
- **Lightweight encapsulation** (hide implementation details)

### 💡 Real-World Example
```python
def make_counter(start=0):
    count = start
    def increment(step=1):
        nonlocal count
        count += step
        return count
    return increment

# Create two independent counters
counter1 = make_counter(10)
counter2 = make_counter(100)

print(counter1())  # 11
print(counter1(5)) # 16
print(counter2())  # 101
```

### 🎨 Visual Explanation
```
make_counter(10) creates:
┌─────────────────┐
│ count = 10      │ ← Captured variable
│                 │
│ increment() ────┼─── Returns this function
│   remembers     │    that remembers count
│   count = 10    │
└─────────────────┘
```

---

## 🎁 Function Decorators

**What is it?** A way to "wrap" functions with extra behavior (like gift wrapping 🎁).

### 🧠 Mental Model
```python
@my_decorator
def my_function():
    return "Hello"

# Is the same as:
my_function = my_decorator(my_function)
```

### 🎯 Why Use Decorators?
- **Add logging** to functions
- **Measure performance** (timing)
- **Add security checks** (authentication)
- **Cache results** (memoization)
- **Retry failed operations**

### 💡 Real-World Examples

#### Basic Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Before function runs
# Hello, Alice!
# After function runs
```

#### Timer Decorator
```python
import time
import functools

def timer(func):
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

slow_function()  # slow_function took 1.000123 seconds
```

#### Stacking Decorators (Like Cake Layers 🎂)
```python
@timer
@logger
def important_function():
    return "Important work done!"

# This applies: timer(logger(important_function))
```

---

## 🏗️ Class Decorators

**What is it?** A decorator that modifies classes instead of functions.

### 🧠 Mental Model
```python
@my_class_decorator
class MyClass:
    pass

# Is the same as:
MyClass = my_class_decorator(MyClass)
```

### 💡 Real-World Examples

#### Auto-Repr Decorator
```python
def auto_repr(cls):
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

@auto_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person)  # Person(name='Alice', age=30)
```

#### Registry Pattern
```python
REGISTRY = {}

def register(cls):
    REGISTRY[cls.__name__] = cls
    return cls

@register
class Dog:
    pass

@register
class Cat:
    pass

print(REGISTRY)  # {'Dog': <class '__main__.Dog'>, 'Cat': <class '__main__.Cat'>}
```

---

## 🔄 Higher-Order Functions

**What is it?** Functions that take other functions as arguments or return functions.

### 🎯 The Big Three: map, filter, reduce

#### Map - Transform Every Item
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

#### Filter - Keep Only What You Want
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

#### Reduce - Combine Everything
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda acc, x: acc + x, numbers, 0)
print(sum_all)  # 15
```

### 🔗 Function Composition
```python
def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def multiply_two(x):
    return x * 2

# Create a pipeline: multiply by 2, then add 1
pipeline = compose(add_one, multiply_two)
print(pipeline(5))  # 11 (5 * 2 + 1)
```

### 🎨 Visual Pipeline
```
Data → [filter] → [map] → [reduce] → Result
  ↓       ↓        ↓        ↓
[1,2,3] → [2] → [4] → 4
```

---

## ✨ Advanced Comprehensions

**What is it?** Concise ways to create lists, dictionaries, and sets.

### 📝 List Comprehensions
```python
# Basic
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested (flatten matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 📚 Dictionary Comprehensions
```python
# Word frequency
text = "to be or not to be"
freq = {word: text.split().count(word) for word in set(text.split())}
print(freq)  # {'to': 2, 'be': 2, 'or': 1, 'not': 1}

# Square mapping
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 🎯 Set Comprehensions
```python
# Unique normalized words
words = {"  Hello  ", "  world  ", "  HELLO  ", "  Python  "}
normalized = {word.strip().lower() for word in words}
print(normalized)  # {'hello', 'world', 'python'}
```

---

## 🔧 Partial Functions

**What is it?** Pre-fill some arguments of a function to create a specialized version.

### 🧠 Mental Model
```python
from functools import partial

def multiply(x, y):
    return x * y

# Create specialized functions
double = partial(multiply, 2)      # Always multiply by 2
triple = partial(multiply, 3)      # Always multiply by 3

print(double(5))   # 10 (2 * 5)
print(triple(4))   # 12 (3 * 4)
```

### 💡 Real-World Examples
```python
# Math functions
def power(base, exponent):
    return base ** exponent

square = partial(power, exp=2)  # Always square
cube = partial(power, exp=3)    # Always cube

print(square(5))  # 25
print(cube(2))    # 8

# String operations
join_with_dash = partial(str.join, '-')
words = ['hello', 'world', 'python']
result = join_with_dash(words)
print(result)  # 'hello-world-python'
```

---

## ⚡ Caching (lru_cache)

**What is it?** Remember function results to avoid recalculating them.

### 🧠 Mental Model
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    # This only runs once per unique input
    return n * n * n

# First call: calculates
result1 = expensive_function(5)  # Calculates 125

# Second call: returns cached result
result2 = expensive_function(5)  # Returns 125 from cache!
```

### 💡 Real-World Example: Fibonacci
```python
import time
from functools import lru_cache

# Without caching (slow)
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# With caching (fast)
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

# Compare performance
start = time.time()
result1 = fib_slow(25)
time1 = time.time() - start

start = time.time()
result2 = fib_fast(35)  # Even larger number!
time2 = time.time() - start

print(f"Slow: {result1} in {time1:.3f}s")
print(f"Fast: {result2} in {time2:.3f}s")
```

### 🎯 When to Use Caching
- **Pure functions** (same input always gives same output)
- **Expensive calculations** (math, API calls, file operations)
- **Recursive functions** (like Fibonacci, factorial)

---

## 🔄 Advanced Iterators & Generators

**What is it?** Ways to process data lazily (one item at a time) instead of loading everything into memory.

### 🎯 Iterator Class
```python
class CountUp:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_count:
            raise StopIteration
        self.current += 1
        return self.current

# Usage
counter = CountUp(5)
for num in counter:
    print(num)  # 1, 2, 3, 4, 5
```

### 🎯 Generator Function
```python
def count_up(max_count):
    current = 0
    while current < max_count:
        current += 1
        yield current  # Pauses here, returns value

# Usage
for num in count_up(5):
    print(num)  # 1, 2, 3, 4, 5
```

### 🔗 Generator Pipeline
```python
def read_numbers(lines):
    for line in lines:
        yield int(line.strip())

def filter_evens(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

# Chain them together
data = ["1", "2", "3", "4", "5", "6"]
pipeline = square_numbers(filter_evens(read_numbers(data)))
result = list(pipeline)
print(result)  # [4, 16, 36] (even numbers squared)
```

### 🎨 Memory Efficiency
```
Traditional approach:
[1,2,3,4,5,6,7,8,9,10] → [2,4,6,8,10] → [4,16,36,64,100] → 15 items in memory

Generator approach:
1 → 2 → 4 (only 1 item in memory at a time)
2 → 4 → 16
3 → (filtered out)
4 → 4 → 16
...
```

---

## 🛡️ Context Managers

**What is it?** Ensure resources are properly cleaned up using the `with` statement.

### 🧠 Mental Model
```python
with open('file.txt') as f:
    content = f.read()
# File is automatically closed here, even if an error occurs!
```

### 🎯 Why Use Context Managers?
- **Automatic cleanup** (files, database connections, locks)
- **Error safety** (cleanup happens even if exceptions occur)
- **Resource management** (memory, network connections)

### 💡 Real-World Examples

#### File Handling
```python
# Without context manager (risky)
f = open('data.txt', 'w')
f.write('Hello World')
f.close()  # What if an error occurs before this?

# With context manager (safe)
with open('data.txt', 'w') as f:
    f.write('Hello World')
# File is automatically closed, even if an error occurs
```

#### Custom Context Manager
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label="Operation"):
    start = time.perf_counter()
    try:
        yield  # This is where your code runs
    finally:
        end = time.perf_counter()
        print(f"{label} took {end - start:.6f} seconds")

# Usage
with timer("Data processing"):
    # Your code here
    time.sleep(1)
    print("Processing complete")
# Output: Data processing took 1.000123 seconds
```

#### Class-based Context Manager
```python
class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.host}:{self.port}")
        self.connection = f"Connection to {self.host}:{self.port}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        self.connection = None

# Usage
with DatabaseConnection("localhost", 5432) as db:
    print(f"Using: {db}")
    # Database operations here
# Connection automatically closed
```

---

## 🚀 Quick Reference

| Concept | When to Use | Key Benefit |
|---------|-------------|-------------|
| **Closures** | Need stateful functions | Lightweight state management |
| **Decorators** | Add behavior to functions | Code reuse, separation of concerns |
| **Class Decorators** | Modify classes | Auto-registration, method injection |
| **HOFs** | Data transformation pipelines | Functional programming style |
| **Comprehensions** | Create collections concisely | Readable, efficient code |
| **Partial Functions** | Pre-configure functions | Specialized function creation |
| **Caching** | Expensive repeated calculations | Performance optimization |
| **Generators** | Large datasets, lazy evaluation | Memory efficiency |
| **Context Managers** | Resource management | Automatic cleanup, error safety |

---

## 🎯 Practice Exercises

### Beginner
1. Create a closure that remembers a counter
2. Write a decorator that logs function calls
3. Use list comprehension to square even numbers

### Intermediate
1. Build a retry decorator with exponential backoff
2. Create a generator that yields Fibonacci numbers
3. Write a context manager for temporary file operations

### Advanced
1. Implement a caching decorator from scratch
2. Build a pipeline using generators and HOFs
3. Create a class decorator that adds validation

---

## 📖 How to Use This Notebook

1. **Open the Jupyter notebook**: `11_advanced_functions_patterns.ipynb`
2. **Run cells sequentially** - each builds on the previous
3. **Experiment** - modify values and see what happens
4. **Practice** - try the exercises at the end of each section
5. **Apply** - use these patterns in your own projects

---

## 🎉 You're Now a Python Power User!

These 9 concepts will transform how you write Python code:
- **Cleaner** - Less boilerplate, more expressive
- **Faster** - Better performance with caching and generators  
- **Safer** - Proper resource management with context managers
- **More Reusable** - Decorators and closures for modular code

Happy coding! 🐍✨
