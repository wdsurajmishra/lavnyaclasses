## sets.md — Set theory and examples

This file explains Python sets: unordered collections of unique, hashable items. It covers creation, common operations, set algebra (union/intersection/difference), comprehension, and important caveats.

### What is a set?

A set is an unordered collection of unique elements. Sets are mutable (you can add and remove items), but their elements must be hashable (immutable types like numbers, strings, tuples). Use sets when you need membership tests, deduplication, or set algebra.

Example:

```py
fruits = {"apple", "banana", "cherry"}
empty = set()       # empty set — use set() not {}
dups = {1, 2, 2, 3} # duplicates are removed: {1, 2, 3}
```

### Creating sets

- Literal: `{1, 2, 3}`
- `set(iterable)`: convert an iterable to a set.

Examples:

```py
s1 = {1, 2, 3}
s2 = set([2, 3, 4])    # from list
s3 = set("hello")     # characters: {'h','e','l','o'}
```

### Basic operations

- `in`: membership test (fast — average O(1)).
- `len(s)`: number of unique elements.
- `add(elem)`: add an element.
- `remove(elem)`: remove element, raises KeyError if not present.
- `discard(elem)`: remove element if present (no error if absent).
- `pop()`: remove and return an arbitrary element (raises KeyError if empty).
- `clear()`: remove all elements.

Examples:

```py
s = {1, 2}
s.add(3)
s.discard(4)   # safe even if 4 not present
# s.remove(4)  # would raise KeyError
item = s.pop() # arbitrary element removed
```

### Set algebra

- `union`: `s1 | s2` or `s1.union(s2)` — elements in either set.
- `intersection`: `s1 & s2` or `s1.intersection(s2)` — elements common to both.
- `difference`: `s1 - s2` or `s1.difference(s2)` — elements in s1 not in s2.
- `symmetric_difference`: `s1 ^ s2` — elements in either set but not both.
- `issubset` / `issuperset` for containment tests.

Examples:

```py
a = {1, 2, 3}
b = {2, 3, 4}
union = a | b                 # {1,2,3,4}
inter = a & b                 # {2,3}
diff = a - b                  # {1}
sym = a ^ b                   # {1,4}
is_sub = {1,2}.issubset(a)    # True
```

### Set comprehensions

Similar to list comprehensions but produce sets.

```py
squares = {x*x for x in range(6)}   # {0,1,4,9,16,25}
```

### Frozen sets

`frozenset(iterable)` creates an immutable set. Useful as dictionary keys or when you need an immutable set.

```py
fs = frozenset([1,2,3])
# fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
```

### Important caveats

- Sets are unordered; iteration order is arbitrary and may change.
- Elements must be hashable. Mutable types like lists cannot be set elements; use tuples instead.
- Because sets are unordered and unindexed, you cannot access elements by position.
- `set()` of an empty dict literal `{}` would create a dict, so use `set()` for empty set.

### Performance notes

- Membership tests (`in`) and adding/removing are on average O(1).
- Set operations (union/intersection/difference) are implemented efficiently in C and are usually faster than doing equivalent list-based operations for membership-heavy use-cases.

### Quick reference

Operation | Example | Result
:--|:--|:--
create | `{1,2}` or `set([1,2])` | set of ints
add | `s.add(x)` | adds x
remove | `s.remove(x)` | removes x, raises KeyError if absent
discard | `s.discard(x)` | removes x if present
union | `s1 | s2` | union set
intersection | `s1 & s2` | intersection set
difference | `s1 - s2` | difference set
sym diff | `s1 ^ s2` | symmetric difference
frozenset | `frozenset([1])` | immutable set

### Example: deduplicating a list

```py
items = [1,2,2,3,3,3]
unique = list(set(items))  # [1,2,3] — order not preserved
```

### Further reading

- Official Python tutorial: Data Structures — sets
- Python documentation: `set` and `frozenset` types

---

If you'd like, I can add `set_examples.py` demonstrating each operation or unit tests for common set behaviors — tell me which you'd prefer.
