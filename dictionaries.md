## dictionaries.md — Dictionary theory and examples

This file explains Python dictionaries (mappings) with creation, access, mutation, iteration, comprehension, common methods, and tips. Dictionaries map immutable keys to values and are Python's primary associative array type.

### What is a dictionary?

A dictionary is an unordered (in older versions), keyed collection that maps unique keys to values. Since Python 3.7 the insertion order of keys is preserved as an implementation detail (and is part of the language spec in 3.8+). Keys must be hashable (immutable types like strings, numbers, tuples).

Example:

```py
person = {"name": "Alice", "age": 30}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
```

### Accessing values

- `d[key]` returns the value or raises KeyError if key absent.
- `d.get(key, default=None)` returns value or default if key not present.
- `d.setdefault(key, default)` returns value if existing, otherwise inserts key with default and returns it.

Examples:

```py
d = {"a": 1}
v = d["a"]          # 1
v2 = d.get("b", 0)  # 0 (safe)
d.setdefault("c", [])  # creates key 'c' with [] and returns it
```

### Adding and updating

- `d[key] = value` assigns or updates.
- `d.update(other)` merges another mapping or iterable of pairs.

```py
 d = {}
 d["x"] = 10
 d.update({"y": 20})
```

### Removing items

- `pop(key[, default])` removes and returns value for key; if key missing and default not provided, raises KeyError.
- `popitem()` removes and returns the last inserted (since 3.7) key-value pair — raises KeyError if empty.
- `clear()` removes all items.

Examples:

```py
d = {"a":1, "b":2}
val = d.pop("a")    # val==1
# d.pop("x")  # raises KeyError
pair = d.popitem()   # ('b', 2)
```

### Iterating dictionaries

- `for k in d:` iterates keys.
- `for k, v in d.items():` iterates key/value pairs.
- `d.keys()` and `d.values()` return view objects.

```py
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)
```

### Dictionary comprehensions

```py
squares = {x: x*x for x in range(6)}
```

### Nested dictionaries and complex values

Dictionaries commonly contain nested dicts or lists. Access nested values carefully (KeyError risk) or use helper utilities.

```py
db = {"user": {"name":"Alice", "roles":["admin"]}}
name = db["user"]["name"]
```

### Copying dictionaries

- `d.copy()` returns a shallow copy. For deep copies of nested data, use `copy.deepcopy()` from the `copy` module.

### Useful patterns and helpers

- `collections.defaultdict` for dictionaries with default factory values (avoid repeated `setdefault` patterns).
- `collections.Counter` for counting hashable items.
- Using tuples (or other hashables) as keys for compound keys.

Example: defaultdict

```py
from collections import defaultdict
dd = defaultdict(list)
dd["a"].append(1)  # no KeyError; dd['a'] becomes [] then appended
```

### Important caveats

- Keys must be hashable. Mutable types (lists, dicts, sets) cannot be used as keys.
- `d[key]` raises KeyError if key missing; use `.get()` when a missing key is possible.
- Iteration over `keys()` or `items()` provides a dynamic view — modifying the dict while iterating can lead to runtime errors.
- Since Python 3.7 insertion order is preserved, but dictionaries are not sets — they map keys to values.

### Quick reference

Operation | Example | Result
:--|:--|:--
create | `{}` or `dict(a=1)` | new dict
access | `d[k]` | value or KeyError
safe get | `d.get(k, default)` | value or default
set | `d[k] = v` | assign value
update | `d.update(other)` | merge mapping
pop | `d.pop(k)` | remove and return value
popitem | `d.popitem()` | remove and return last (k,v)
keys/items/values | `d.keys()` | view objects
copy | `d.copy()` | shallow copy

### Example: grouping items

```py
data = [("a",1),("b",2),("a",3)]
grouped = {}
for k,v in data:
    grouped.setdefault(k, []).append(v)

# grouped == {'a':[1,3], 'b':[2]}
```

### Further reading

- Official Python tutorial: Data Structures — dictionaries
- Python documentation: `dict` built-in type and `collections` module

---

If you want, I can also add `dict_examples.py` demonstrating safe access, `defaultdict`, and common pitfalls or write a tiny test file showing the behaviors above.
