## input.md — Quick notes on reading input in Python

Short reference for reading user input in Python (Python 3.x).

### Basics

- input(prompt) reads a line from standard input, displays optional prompt, and returns a string (without the trailing newline).

Example:

```py
name = input("Enter your name: ")
print("Hello,", name)
```

### Type conversion

input() always returns a string. Convert when you need numbers or other types:

```py
age = int(input("Age: "))
coords = tuple(map(float, input("x y:").split()))
```

Wrap conversions in try/except to handle invalid input.

### Multiple values

Use split() to accept multiple space-separated values, or use csv parsing for complex formats.

```py
nums = list(map(int, input().split()))  # read a line of ints
```

### Validation and loops

Common pattern: loop until valid input is received.

```py
while True:
    s = input("Enter a positive integer: ")
    try:
        n = int(s)
        if n > 0:
            break
    except ValueError:
        pass
    print("Invalid — try again.")
```

### EOF and interruptions

- input() raises EOFError on end-of-file (e.g., when stdin is closed or input redirected ends).
- KeyboardInterrupt is raised when user hits Ctrl+C. Catch these if you need graceful shutdown.

### Security

- Never use eval() on raw input; treat input as untrusted. Parse and validate instead.

### Advanced: non-interactive input

- When a script is used in pipelines or with redirected files, input() reads from stdin. Consider using sys.stdin when you need streaming reads.

```py
import sys
for line in sys.stdin:
    process(line.strip())
```

### Passwords

Use getpass.getpass() to securely read passwords without echoing to the terminal.

### Quick tips

- Use prompt text that makes valid format clear.
- Strip and validate input early (e.g., s = input().strip()).
- For command-line scripts with many options, prefer argparse over input().

---

This is a short notes file — if you want, I can add a small `input_examples.py` demonstrating each pattern, or expand this file with common validation helpers.
