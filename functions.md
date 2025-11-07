## Python functions — reference

This document is a compact but thorough reference for Python functions. It covers definition and calling, parameter types, default values, variable arguments, annotations and typing, scope and closures, lambdas, higher-order functions, decorators, recursion, best practices, and examples.

---

### 1. Defining a function

Use the `def` keyword. A function may return a value with `return` (or `None` implicitly).

```py
def greet(name):
    """Return a greeting for name."""
    return f"Hello, {name}!"

print(greet("Suraj"))  # Hello, Suraj!
```

Functions are objects: you can assign them, pass them, and store them in containers.

```py
f = greet
print(f("Ada"))
```

### 2. Parameters and calling

Parameter kinds supported by Python (in order of appearance in a signature):

- Positional-only parameters (Python 3.8+ with `/`).
- Positional-or-keyword parameters (the normal case).
- Default parameters: `x=1`.
- Variable positional args: `*args` collects extra positional arguments as a tuple.
- Keyword-only parameters: placed after a `*` or `*args` in the signature.
- Variable keyword args: `**kwargs` collects extra keyword args as a dict.

Example signature:

```py
def example(a, b=2, *args, c, d=4, **kwargs):
    pass
```

Calling rules:

- You can supply positional and/or keyword arguments.
- Extra positional arguments go into `args`; extra keyword args go into `kwargs`.
- Keyword-only arguments must be passed by name.

Example:

```py
def add(a, b=0):
    return a + b

add(1, 2)    # 3
add(1)       # 1
add(a=5, b=6) # 11
```

### 3. Default argument gotcha

Default values are evaluated once at function definition time. Avoid using mutable objects (like lists or dicts) as defaults unless you intentionally want sharing behavior.

Bad pattern:

```py
def append_bad(x, lst=[]):
    lst.append(x)
    return lst

append_bad(1)  # [1]
append_bad(2)  # [1, 2]  -- unexpected shared list
```

Correct pattern:

```py
def append_good(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
```

### 4. Argument unpacking

Use `*` and `**` to unpack sequences and mappings into function calls.

```py
def f(a, b, c):
    return a + b + c

vals = (1, 2, 3)
f(*vals)  # 6

kwargs = {"a": 10, "b": 20, "c": 30}
f(**kwargs)  # 60
```

### 5. Annotations and typing

Function annotations provide optional type hints and other metadata. Use the `typing` module for richer types.

```py
from typing import List, Tuple

def sum_list(nums: List[int]) -> int:
    return sum(nums)

def lookup(name: str) -> Tuple[str, int]:
    return (name, len(name))
```

Annotations are not enforced at runtime by default. Use tools like `mypy` or `pyright` for static checking.

### 6. Docstrings and introspection

Write docstrings (PEP 257) to explain function behavior, arguments, return values, and exceptions.

```py
def foo(x: int) -> int:
    """Square x.

    Args:
        x: integer to square

    Returns:
        x squared
    """
    return x * x

print(foo.__doc__)
```

### 7. Scope, locals, and globals

Python uses lexical scoping. `global` declares that a name refers to module-level binding. `nonlocal` (Python 3) allows modification of outer non-global variables (useful for closures).

```py
def outer():
    x = 0

    def inner():
        nonlocal x
        x += 1
        return x

    return inner

c = outer()
print(c())  # 1
print(c())  # 2
```

Avoid overusing `global`. Prefer returning values and passing parameters.

### 8. Closures

A closure is a function that remembers variables from its enclosing scope.

```py
def multiplier(n):
    def mul(x):
        return x * n
    return mul

double = multiplier(2)
print(double(5))  # 10
```

Closures are frequently used to parameterize behavior without global state.

### 9. Lambda (anonymous) functions

Use `lambda` for short single-expression functions. Prefer named functions for complex logic.

```py
square = lambda x: x * x
print(square(4))  # 16

# Common use in higher-order functions:
nums = [1, 2, 3]
print(list(map(lambda x: x*x, nums)))
```

### 10. Higher-order functions

Functions that accept or return other functions are common.

```py
def apply_twice(f, x):
    return f(f(x))

print(apply_twice(lambda x: x+2, 3))  # 7
```

`map`, `filter`, and `functools.reduce` are built-ins for functional-style transforms.

### 11. Decorators

Decorators wrap a function to modify or extend behavior. They are functions that take a function and return a new one. Use `functools.wraps` to preserve metadata.

Simple decorator:

```py
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(2, 3)
```

Decorators can accept arguments (create a decorator factory).

### 12. Recursion

Functions may call themselves. Ensure a base case to avoid infinite recursion. Python's recursion depth is limited (default ~1000).

```py
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
```

For deep recursion consider iterative solutions or `sys.setrecursionlimit()` (use cautiously).

### 13. Generators and `yield`

Generators are functions that yield values instead of returning them. They produce iterators and allow lazily producing sequences.

```py
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)
```

Use `yield from` to delegate to sub-generators.

### 14. Async functions (coroutines)

Use `async def` to define coroutines for asynchronous programming (requires `await`, `asyncio` event loop).

```py
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    await asyncio.gather(say_after(1, "hello"), say_after(2, "world"))

# asyncio.run(main())
```

### 15. Best practices

- Keep functions short and focused (single responsibility). Prefer 20–30 lines max where practical.
- Use descriptive names for functions and parameters.
- Document public functions with docstrings (describe args, returns, raises).
- Prefer `None` as default for optional mutable parameters.
- Use type hints for public APIs and run a static type checker.
- Avoid side effects when possible; prefer returning new values.
- Use tests for complex functions and edge cases.

### 16. Common examples

1) Safe default and varargs:

```py
def collect(prefix, *items, container=None):
    if container is None:
        container = []
    container.extend(items)
    return prefix, container

print(collect("x", 1, 2, 3))
```

2) Decorator with parameter:

```py
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("hi")
```

3) Returning multiple values (tuples):

```py
def min_max(seq):
    return min(seq), max(seq)

low, high = min_max([3, 1, 4])
```

### 17. Testing functions

- Write unit tests for normal flows and edge cases.
- Use parameterized tests (pytest) for multiple inputs.

Example (pytest):

```py
def test_sum_list():
    assert sum_list([1,2,3]) == 6

@pytest.mark.parametrize("inp,expected", [([1],1),([2,3],5)])
def test_sum_param(inp, expected):
    assert sum(inp) == expected
```

---

If you'd like, I can:

1. Add a `function_examples.py` with runnable examples for many of the patterns above.
2. Add unit tests (`tests/test_functions.py`) demonstrating expected behavior.
3. Add a short cheatsheet PDF or printable version.

Tell me which you'd like and I'll create it.
