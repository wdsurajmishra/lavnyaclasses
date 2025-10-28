## tuple.md — Tuple theory and examples

This file explains Python tuples with clear theory, examples, and notes. It mirrors the style used for other reference files in this workspace and targets beginners.

### What is a tuple?

A tuple is an ordered, immutable collection of values. Tuples are similar to lists but cannot be changed after they are created (no item assignment, append, or remove). Tuples are used when immutability is desired — for example, representing fixed records.

Example:

```py
point = (10, 20)
colors = ("red", "green", "blue")
empty = ()
```

### Creating tuples

- Parentheses are common but optional for simple cases.
- Use a trailing comma for single-element tuples.

Examples:

```py
t1 = (1, 2, 3)
t2 = 4, 5, 6        # parentheses optional
single = (42,)       # single-element tuple — comma is required
not_a_tuple = (42)   # this is an int, not a tuple
```

### Tuple packing and unpacking

Packing groups values into a tuple. Unpacking assigns tuple items to variables.

```py
packed = 1, 2, "three"   # packing
a, b, c = packed          # unpacking: a=1, b=2, c="three"

# You can also unpack into (possibly) fewer variables using star-unpacking
head, *tail = (10, 20, 30, 40)  # head=10, tail=[20,30,40]
```

Note: star-unpacking produces a list for the starred variable.

### Accessing items

Indexing and slicing work the same as for lists.

```py
names = ("Alice", "Bob", "Charlie")
first = names[0]      # 'Alice'
last = names[-1]      # 'Charlie'
slice_ = names[0:2]   # ('Alice', 'Bob') — slicing returns a tuple
```

### Immutability

Tuples cannot be changed after creation. Attempts to assign to an index raise a TypeError.

```py
nums = (1, 2, 3)
# nums[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

However, if a tuple contains a mutable object (for example a list), that inner object can be mutated:

```py
t = (1, [2, 3])
t[1].append(4)   # allowed — the list inside the tuple is mutable
```

### Common tuple operations

- Concatenation: `t1 + t2` produces a new tuple.
- Repetition: `t * 3` repeats contents.
- Membership: `x in t` checks presence.
- Length: `len(t)` returns number of items.

Examples:

```py
t1 = (1, 2)
t2 = (3,) 
combined = t1 + t2     # (1, 2, 3)
repeated = t1 * 2       # (1, 2, 1, 2)
is_present = 2 in t1    # True
count = len(t1)         # 2
```

### Tuple methods

Tuples have only a few built-in methods because they are immutable.

- `count(value)` — returns how many times value appears.
- `index(value)` — returns the index of the first occurrence (raises ValueError if not found).

Example:

```py
t = (1, 2, 2, 3)
t.count(2)   # 2
t.index(3)   # 3
```

### Converting between tuples and lists

You can convert a tuple to a list to make modifications, then convert back to a tuple.

```py
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t2 = tuple(lst)  # (1, 2, 3, 4)
```

### Nested tuples

Tuples can contain other tuples (or lists and other objects).

```py
matrix = ((1,2,3), (4,5,6), (7,8,9))
element = matrix[1][2]  # 6
```

### Use-cases for tuples

- Fixed collections of heterogeneous values, e.g., (x, y) coordinates, rows from a database, or function returns.
- Keys in dictionaries when an immutable compound key is needed.
- Slight performance and memory advantage over lists for small, fixed sequences.

### Edge cases and tips

- Single-element tuples must have a trailing comma: `(value,)`.
- Parentheses are optional for tuple literals, but they help readability and are required in some contexts (e.g., empty tuple `()`).
- Methods that return modified sequences for lists (like `.append()` or `.sort()`) do not exist for tuples because tuples are immutable.
- When unpacking, ensure the number of variables matches the tuple structure (or use star `*` to collect remaining items).

### Quick reference

Operation | Example | Result
:--|:--|:--
create | `(1, 2)` or `1, 2` | tuple of two ints
single element | `(1,)` | single-element tuple
index | `t[0]` | first element
slice | `t[1:3]` | tuple slice
concat | `t1 + t2` | new tuple
repeat | `t * 3` | repeated tuple
len | `len(t)` | length
in | `x in t` | membership boolean
count | `t.count(x)` | number of occurrences
index method | `t.index(x)` | first index of x

### Example: function returning multiple values

```py
def min_max(seq):
    return (min(seq), max(seq))

low, high = min_max([4, 1, 9, 2])  # tuple returned and unpacked
```

### Further reading

- Official Python tutorial: Data Structures — tuples
- Python documentation: `tuple` built-in type

---

If you'd like, I can also: add short runnable examples in a `tuple_examples.py`, add unit tests demonstrating tuple behavior, or add links to official docs directly in this file. Tell me which you'd prefer.
