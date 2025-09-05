# Lesson 02: Data Types

## Table of Contents
1. [Introduction to Data Types](#introduction-to-data-types)
2. [Numeric Types](#numeric-types)
3. [Boolean Type](#boolean-type)
4. [Sequence Types](#sequence-types)
5. [Set Types](#set-types)
6. [Mapping Type](#mapping-type)
7. [Binary Types](#binary-types)
8. [Number Systems](#number-systems)
9. [Type Checking and Conversion](#type-checking-and-conversion)
10. [Useful Links](#useful-links)

---

## Introduction to Data Types

### Theory
Data types determine the type of value a variable can hold and the operations that can be performed on it. They define the format, structure, size, range, and behavior of data, controlling how it's stored and used in a program. This helps ensure data is used correctly and efficiently, providing type safety and enabling the Python interpreter to optimize memory usage and operations.

### Python Data Types Overview
```mermaid
graph TD
    A["Python Data Types"] --> B["Numeric Types"]
    A --> C["Boolean Type"]
    A --> D["Sequence Types"]
    A --> E["Set Types"]
    A --> F["Mapping Type"]
    A --> G["Binary Types"]
    
    B --> B1["int - Integer"]
    B --> B2["float - Floating Point"]
    B --> B3["complex - Complex Number"]
    
    C --> C1["bool - True/False"]
    
    D --> D1["str - String"]
    D --> D2["list - Mutable List"]
    D --> D3["tuple - Immutable Tuple"]
    D --> D4["range - Number Range"]
    
    E --> E1["set - Mutable Set"]
    E --> E2["frozenset - Immutable Set"]
    
    F --> F1["dict - Dictionary"]
    
    G --> G1["bytes - Immutable Bytes"]
    G --> G2["bytearray - Mutable Bytes"]
    G --> G3["memoryview - Memory View"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
    style F fill:#ff99cc
    style G fill:#99ffcc
```

### Data Type Characteristics
```mermaid
mindmap
  root((Data Type Characteristics))
    Mutability
      Mutable
        list
        dict
        set
        bytearray
      Immutable
        int
        float
        str
        tuple
        frozenset
        bytes
    Ordering
      Ordered
        list
        tuple
        str
        range
        dict
      Unordered
        set
        frozenset
    Uniqueness
      Unique Elements
        set
        frozenset
      Duplicates Allowed
        list
        tuple
        str
        dict
    Indexing
      Indexable
        list
        tuple
        str
        range
        bytes
        bytearray
      Non-Indexable
        set
        frozenset
        dict
```

---

## Numeric Types

### Theory
Python provides three main numeric types to handle different kinds of numbers. These types support various mathematical operations and are essential for calculations, scientific computing, and data analysis. Each numeric type has specific characteristics regarding precision, range, and use cases.

### Numeric Types Overview
```mermaid
graph TD
    A["Numeric Types"] --> B["Integer (int)"]
    A --> C["Float (float)"]
    A --> D["Complex (complex)"]
    
    B --> B1["Whole Numbers"]
    B --> B2["Positive/Negative"]
    B --> B3["Unlimited Precision"]
    B --> B4["Examples: 42, -17, 0"]
    
    C --> C1["Decimal Numbers"]
    C --> C2["Scientific Notation"]
    C --> C3["Limited Precision"]
    C --> C4["Examples: 3.14, -2.5, 1e5"]
    
    D --> D1["Real + Imaginary"]
    D --> D2["Mathematical Operations"]
    D --> D3["Scientific Computing"]
    D --> D4["Examples: 2+3j, 1-4j"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Integer Type Details
```mermaid
graph LR
    A["Integer (int)"] --> B["Characteristics"]
    A --> C["Operations"]
    A --> D["Use Cases"]
    
    B --> B1["Unlimited Precision"]
    B --> B2["Memory Efficient"]
    B --> B3["Base Support"]
    
    C --> C1["Arithmetic: +, -, *, /"]
    C --> C2["Comparison: <, >, ==, !="]
    C --> C3["Bitwise: &, |, ^, ~"]
    
    D --> D1["Counting"]
    D --> D2["Indexing"]
    D --> D3["Mathematical Calculations"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Float Type Details
```mermaid
graph LR
    A["Float (float)"] --> B["Characteristics"]
    A --> C["Precision"]
    A --> D["Representation"]
    
    B --> B1["64-bit Double Precision"]
    B --> B2["IEEE 754 Standard"]
    B --> B3["Scientific Notation"]
    
    C --> C1["~15-17 Decimal Digits"]
    C --> C2["Floating Point Errors"]
    C --> C3["Rounding Issues"]
    
    D --> D1["Decimal: 3.14159"]
    D --> D2["Scientific: 1.23e-4"]
    D --> D3["Exponential: 2.5E+3"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Complex Number Details
```mermaid
graph TD
    A["Complex (complex)"] --> B["Structure"]
    A --> C["Properties"]
    A --> D["Operations"]
    
    B --> B1["Real Part: z.real"]
    B --> B2["Imaginary Part: z.imag"]
    B --> B3["Format: a + bj"]
    
    C --> C1["Mathematical Functions"]
    C --> C2["Conjugate: z.conjugate()"]
    C --> C3["Magnitude: abs(z)"]
    
    D --> D1["Addition: (a+bj) + (c+dj)"]
    D --> D2["Multiplication: (a+bj) * (c+dj)"]
    D --> D3["Division: (a+bj) / (c+dj)"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Boolean Type

### Theory
The Boolean type in Python represents truth values and is fundamental to control flow and logical operations. It has only two possible values: `True` and `False`. Booleans are essential for conditional statements, loops, and logical operations that control program execution.

### Boolean Type Overview
```mermaid
graph TD
    A["Boolean (bool)"] --> B["Values"]
    A --> C["Operations"]
    A --> D["Use Cases"]
    
    B --> B1["True"]
    B --> B2["False"]
    B --> B3["Case Sensitive"]
    
    C --> C1["Logical: and, or, not"]
    C --> C2["Comparison: ==, !=, <, >"]
    C --> C3["Identity: is, is not"]
    
    D --> D1["Conditional Statements"]
    D --> D2["Loop Control"]
    D --> D3["Function Returns"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Boolean Operations
```mermaid
graph LR
    A["Boolean Operations"] --> B["Logical Operators"]
    A --> C["Comparison Operators"]
    A --> D["Identity Operators"]
    
    B --> B1["and: Both True"]
    B --> B2["or: Either True"]
    B --> B3["not: Invert Value"]
    
    C --> C1["==: Equal"]
    C --> C2["!=: Not Equal"]
    C --> C3["<, >, <=, >="]
    
    D --> D1["is: Same Object"]
    D --> D2["is not: Different Object"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Sequence Types

### Theory
Sequence types in Python are ordered collections that can contain multiple items. They support indexing, slicing, and iteration. Python provides several built-in sequence types, each with different characteristics regarding mutability and use cases.

### Sequence Types Overview
```mermaid
graph TD
    A["Sequence Types"] --> B["String (str)"]
    A --> C["List (list)"]
    A --> D["Tuple (tuple)"]
    A --> E["Range (range)"]
    
    B --> B1["Immutable"]
    B --> B2["Character Sequence"]
    B --> B3["Text Processing"]
    
    C --> C1["Mutable"]
    C --> C2["Heterogeneous"]
    C --> C3["Dynamic Sizing"]
    
    D --> D1["Immutable"]
    D --> D2["Heterogeneous"]
    D --> D3["Fixed Size"]
    
    E --> D1["Immutable"]
    E --> D2["Numeric Sequence"]
    E --> D3["Memory Efficient"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

### String Type Details
```mermaid
graph TD
    A["String (str)"] --> B["Creation Methods"]
    A --> C["Properties"]
    A --> D["Operations"]
    
    B --> B1["Single Quotes: 'text'"]
    B --> B2["Double Quotes: \"text\""]
    B --> B3["Triple Quotes: '''text'''"]
    
    C --> C1["Immutable"]
    C --> C2["Unicode Support"]
    C --> C3["Indexable"]
    
    D --> D1["Concatenation: +"]
    D --> D2["Repetition: *"]
    D --> D3["Slicing: [start:end]"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### List vs Tuple Comparison
```mermaid
graph LR
    A["List vs Tuple"] --> B["List (list)"]
    A --> C["Tuple (tuple)"]
    
    B --> B1["Mutable"]
    B --> B2["Square Brackets: []"]
    B --> B3["Dynamic Size"]
    B --> B4["Methods: append(), remove()"]
    
    C --> C1["Immutable"]
    C --> C2["Parentheses: ()"]
    C --> C3["Fixed Size"]
    C --> C4["No Modification Methods"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
```

---

## Set Types

### Theory
Set types in Python represent unordered collections of unique elements. They are useful for mathematical set operations, removing duplicates, and testing membership. Python provides both mutable (`set`) and immutable (`frozenset`) versions.

### Set Types Overview
```mermaid
graph TD
    A["Set Types"] --> B["Set (set)"]
    A --> C["Frozen Set (frozenset)"]
    
    B --> B1["Mutable"]
    B --> B2["Curly Braces: {}"]
    B --> B3["Add/Remove Elements"]
    
    C --> C1["Immutable"]
    C --> C2["frozenset() Constructor"]
    C --> C3["Fixed Elements"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
```

### Set Operations
```mermaid
graph LR
    A["Set Operations"] --> B["Mathematical"]
    A --> C["Membership"]
    A --> D["Modification"]
    
    B --> B1["Union: | or union()"]
    B --> B2["Intersection: & or intersection()"]
    B --> B3["Difference: - or difference()"]
    
    C --> C1["in: Membership Test"]
    C --> C2["not in: Non-membership"]
    
    D --> D1["add(): Add Element"]
    D --> D2["remove(): Remove Element"]
    D --> D3["clear(): Remove All"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Mapping Type

### Theory
The mapping type in Python is represented by dictionaries (`dict`), which store key-value pairs. Dictionaries are mutable, unordered collections that provide fast lookup, insertion, and deletion operations. They are essential for representing structured data and implementing hash tables.

### Dictionary Type Details
```mermaid
graph TD
    A["Dictionary (dict)"] --> B["Structure"]
    A --> C["Properties"]
    A --> D["Operations"]
    
    B --> B1["Key-Value Pairs"]
    B --> B2["Curly Braces: {}"]
    B --> B3["Colon Separator: key: value"]
    
    C --> C1["Mutable"]
    C --> C2["Unordered (Python 3.7+)"]
    C --> C3["Keys Must Be Hashable"]
    
    D --> D1["Access: dict[key]"]
    D --> D2["Assignment: dict[key] = value"]
    D --> D3["Deletion: del dict[key]"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Dictionary Methods
```mermaid
graph LR
    A["Dictionary Methods"] --> B["Access"]
    A --> C["Modification"]
    A --> D["Information"]
    
    B --> B1["get(): Safe Access"]
    B --> B2["keys(): All Keys"]
    B --> B3["values(): All Values"]
    
    C --> C1["update(): Merge Dictionaries"]
    C --> C2["pop(): Remove & Return"]
    C --> C3["clear(): Remove All"]
    
    D --> D1["len(): Number of Pairs"]
    D --> D2["in: Key Membership"]
    D --> D3["items(): Key-Value Pairs"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Binary Types

### Theory
Binary types in Python handle raw binary data, which is essential for file I/O, network communication, and working with non-text data. Python provides three binary types: `bytes` (immutable), `bytearray` (mutable), and `memoryview` (memory-efficient access).

### Binary Types Overview
```mermaid
graph TD
    A["Binary Types"] --> B["Bytes (bytes)"]
    A --> C["Bytearray (bytearray)"]
    A --> D["Memoryview (memoryview)"]
    
    B --> B1["Immutable"]
    B --> B2["Literal: b'text'"]
    B --> B3["File I/O"]
    
    C --> C1["Mutable"]
    C --> C2["Constructor: bytearray()"]
    C --> C3["Modify in Place"]
    
    D --> D1["Memory Efficient"]
    D --> D2["No Data Copying"]
    D --> D3["Large Data Processing"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Binary Data Operations
```mermaid
graph LR
    A["Binary Operations"] --> B["Creation"]
    A --> C["Conversion"]
    A --> D["Manipulation"]
    
    B --> B1["b'hello': Bytes Literal"]
    B --> B2["bytearray([65,66]): From List"]
    B --> B3["memoryview(data): From Object"]
    
    C --> C1["decode(): Bytes to String"]
    C --> C2["encode(): String to Bytes"]
    C --> C3["chr(): ASCII to Character"]
    
    D --> D1["Indexing: data[0]"]
    D --> D2["Slicing: data[1:3]"]
    D --> D3["Modification: data[0] = 65"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Number Systems

### Theory
Number systems are fundamental to understanding how computers represent and process data. Different number systems (binary, decimal, hexadecimal, octal) are used in various computing contexts, from low-level programming to data representation.

### Number Systems Overview
```mermaid
graph TD
    A["Number Systems"] --> B["Binary (Base 2)"]
    A --> C["Decimal (Base 10)"]
    A --> D["Hexadecimal (Base 16)"]
    A --> E["Octal (Base 8)"]
    
    B --> B1["Digits: 0, 1"]
    B --> B2["Computer Memory"]
    B --> B3["Bit Operations"]
    
    C --> C1["Digits: 0-9"]
    C --> C2["Human Counting"]
    C --> C3["Mathematical Operations"]
    
    D --> D1["Digits: 0-9, A-F"]
    D --> D2["Memory Addresses"]
    D --> D3["Color Codes"]
    
    E --> E1["Digits: 0-7"]
    E --> E2["File Permissions"]
    E --> E3["Legacy Systems"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
    style E fill:#cc99ff
```

### Number System Conversions
```mermaid
graph LR
    A["Conversions"] --> B["Python Functions"]
    A --> C["Base Conversion"]
    A --> D["String Formatting"]
    
    B --> B1["bin(): To Binary"]
    B --> B2["hex(): To Hexadecimal"]
    B --> B3["oct(): To Octal"]
    
    C --> C1["int('1010', 2): Binary to Decimal"]
    C --> C2["int('FF', 16): Hex to Decimal"]
    C --> C3["int('77', 8): Octal to Decimal"]
    
    D --> D1["f'{num:b}': Binary Format"]
    D --> D2["f'{num:x}': Hex Format"]
    D --> D3["f'{num:o}': Octal Format"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### ASCII and Unicode
```mermaid
graph TD
    A["Character Encoding"] --> B["ASCII"]
    A --> C["Unicode"]
    A --> D["UTF-8"]
    
    B --> B1["128 Characters"]
    B --> B2["0-127 Range"]
    B --> B3["English Only"]
    
    C --> C1["Universal Standard"]
    C --> C2["All Languages"]
    C --> C3["Code Points"]
    
    D --> D1["Variable Length"]
    D --> D2["Backward Compatible"]
    D --> D3["Web Standard"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Type Checking and Conversion

### Theory
Python's dynamic typing system allows variables to change types during runtime, but sometimes you need to explicitly convert between types or check the type of a variable. Understanding type checking and conversion is crucial for robust programming.

### Type Checking
```mermaid
graph TD
    A["Type Checking"] --> B["type() Function"]
    A --> C["isinstance() Function"]
    A --> D["Type Hints"]
    
    B --> B1["Returns Type Object"]
    B --> B2["Exact Type Match"]
    B --> B3["type(var) == int"]
    
    C --> C1["Inheritance Aware"]
    C --> C2["Multiple Types"]
    C --> C3["isinstance(var, (int, float))"]
    
    D --> D1["Static Type Hints"]
    D --> D2["IDE Support"]
    D --> D3["Documentation"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Type Conversion
```mermaid
graph LR
    A["Type Conversion"] --> B["Implicit"]
    A --> C["Explicit"]
    A --> D["Functions"]
    
    B --> B1["Automatic Promotion"]
    B --> B2["int + float = float"]
    B --> B3["Safe Conversions"]
    
    C --> C1["Manual Conversion"]
    C --> C2["int(), float(), str()"]
    C --> C3["May Raise Errors"]
    
    D --> D1["int(): To Integer"]
    D --> D2["float(): To Float"]
    D --> D3["str(): To String"]
    D --> D4["list(): To List"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

### Type Conversion Examples
```mermaid
graph TD
    A["Conversion Examples"] --> B["Numeric Conversions"]
    A --> C["String Conversions"]
    A --> D["Collection Conversions"]
    
    B --> B1["int(3.14) → 3"]
    B --> B2["float(42) → 42.0"]
    B --> B3["complex(2, 3) → 2+3j"]
    
    C --> C1["str(123) → '123'"]
    C --> C2["int('456') → 456"]
    C --> C3["float('3.14') → 3.14"]
    
    D --> D1["list('hello') → ['h','e','l','l','o']"]
    D --> D2["tuple([1,2,3]) → (1,2,3)"]
    D --> D3["set([1,1,2,3]) → {1,2,3}"]
    
    style A fill:#ff9999
    style B fill:#99ccff
    style C fill:#99ff99
    style D fill:#ffcc99
```

---

## Useful Links

### Essential Python Resources
- [Python 3.13.2 Documentation - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Data Types Tutorial](https://www.w3schools.com/python/python_datatypes.asp)
- [Real Python - Python Data Types](https://realpython.com/python-data-types/)

### Number Systems and Encoding
- [ASCII Table](https://www.ascii-code.com/)
- [Unicode Standard](https://unicode.org/)
- [UTF-8 Encoding](https://en.wikipedia.org/wiki/UTF-8)

### Type Checking and Validation
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [mypy - Static Type Checker](https://mypy.readthedocs.io/)
- [Pydantic - Data Validation](https://pydantic-docs.helpmanual.io/)

### Learning Resources
- [Python.org Tutorial - Data Types](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [Codecademy - Python Data Types](https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-data-types)
- [Python for Beginners - Data Types](https://www.pythonforbeginners.com/basics/python-data-types)

---

## Summary

This lesson provides a comprehensive overview of Python's built-in data types, covering their characteristics, use cases, and operations. Understanding data types is fundamental to writing effective Python code and choosing the right data structure for your specific needs.

### Key Takeaways
1. **Numeric Types**: `int`, `float`, and `complex` for mathematical operations
2. **Boolean Type**: `bool` for logical operations and control flow
3. **Sequence Types**: `str`, `list`, `tuple`, and `range` for ordered collections
4. **Set Types**: `set` and `frozenset` for unique element collections
5. **Mapping Type**: `dict` for key-value pair storage
6. **Binary Types**: `bytes`, `bytearray`, and `memoryview` for binary data
7. **Type System**: Understanding mutability, ordering, and uniqueness
8. **Number Systems**: Binary, decimal, hexadecimal, and octal representations
9. **Type Operations**: Checking types and converting between them

### Best Practices
- Choose appropriate data types for your use case
- Understand mutability implications
- Use type hints for better code documentation
- Be aware of floating-point precision limitations
- Leverage set operations for unique element handling
- Use dictionaries for structured data representation

---

*Author: Arif Kasim Rozani - (Team Operation Badar)*
