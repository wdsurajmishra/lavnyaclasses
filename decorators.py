def changeCase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


@changeCase
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

# print(greet("Suraj"))

@changeCase
def newGreet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

print(newGreet("Suraj"))