## for & while loops — quick notes

This file is a compact reference for Python `for` and `while` loops with examples, common idioms, pitfalls, and tips.

---

### for loop — basic syntax

```py
for item in iterable:
    # body
    pass
```

- `iterable` can be any object that returns an iterator: lists, tuples, dicts, sets, strings, generators, file objects, etc.
- The loop pulls successive values using the iterator protocol until it is exhausted (StopIteration).

Example:

```py
fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)
```

### Iterating with index: `enumerate()`

Prefer `enumerate()` over manual index handling:

```py
for i, v in enumerate(fruits, start=0):
    print(i, v)
```

### Iterating multiple iterables: `zip()`

```py
names = ["alice", "bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(name, age)
```

Note: `zip()` stops at the shortest iterable. Use `itertools.zip_longest()` to continue.

### Looping over dictionaries

```py
d = {"a": 1, "b": 2}
for k in d:           # iterate keys
    print(k, d[k])

for k, v in d.items():
    print(k, v)
```

### List/set/dict comprehensions (prefer for transformations)

```py
squares = [x*x for x in range(6)]
unique = {x % 3 for x in range(10)}
mapping = {x: x*x for x in range(5)}
```

Comprehensions are often clearer and faster for simple transforms.

### for-else (less common but useful)

The `else` branch runs when the loop completes normally (no `break`).

```py
for x in seq:
    if condition(x):
        found = x
        break
else:
    # runs if loop did NOT encounter break
    found = None
```

### while loop — basic syntax

```py
while condition:
    # body
    pass
```

Use `while` when the number of iterations is not known in advance.

Example (input validation):

```py
while True:
    s = input("Enter positive integer: ")
    try:
        n = int(s)
        if n > 0:
            break
    except ValueError:
        pass
    print("Invalid — try again")

print("Got", n)
```

### while-else

Like `for-else`, the `else` block on a `while` runs if the loop ends without `break`.

```py
i = 0
while i < 5:
    if check(i):
        break
    i += 1
else:
    print("never broke")
```

### break and continue

- `break` exits the nearest loop immediately.
- `continue` skips the remainder of the body and continues with the next iteration.

### Common patterns

- Sentinel loop (useful for reading until sentinel):

```py
for line in iter(lambda: f.readline(), ""):
    process(line)
```

- Using `range()` for numeric loops:

```py
for i in range(0, 10, 2):
    print(i)
```

- Reverse iteration:

```py
for x in reversed(seq):
    print(x)
```

### Nested loops

Nested loops are fine but be mindful of O(n*m) complexity.

```py
for a in A:
    for b in B:
        process(a, b)
```

Break/continue only affect the inner loop unless you restructure control flow.

### Iteration pitfalls & tips

- Do not modify (add/remove) a list while iterating it; iterate over a copy or use list comprehension.

```py
# Bad:
for x in items:
    if need_remove(x):
        items.remove(x)

# Good:
items = [x for x in items if not need_remove(x)]
```

- Use `enumerate()` for index+value; avoid `range(len(seq))` when possible for readability.
- Prefer generator expressions for streaming/transformation without creating intermediate lists: `sum(x*x for x in nums)`.

### Performance notes

- `for` loops in Python are implemented in C but Python-level loop bodies are slower than vectorized operations (NumPy) for numeric work.
- Use local variables in loops (assign attributes to local variables) to minimize attribute lookup cost.

### Infinite loops & graceful shutdown

Be careful with `while True:` loops. Catch `KeyboardInterrupt` or check an external stop condition.

```py
try:
    while True:
        do_work()
except KeyboardInterrupt:
    print("Interrupted")
```

### Advanced helpers

- `itertools` module provides many useful iterator utilities: `chain`, `islice`, `product`, `combinations`, etc.
- `itertools.repeat` + `map`/`filter` can replace some `while` patterns.

---

Quick checklist when writing loops:

- Know whether you need `for` (iterable-driven) or `while` (condition-driven).
- Use `enumerate`, `zip`, `reversed`, `range` for common tasks.
- Avoid changing the iterated object in-place.
- Use comprehensions/generator expressions where appropriate.
- Add comments for complex nested loops; consider extracting into functions.

If you want, I can add `loop_examples.py` with runnable examples and small tests — tell me and I will create it.
