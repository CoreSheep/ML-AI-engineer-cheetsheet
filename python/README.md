# Python Patterns & Solutions

Python best practices, design patterns, and LeetCode solutions.

## Contents

### LeetCode Solutions

**LeetCode_AC_list.md**
- 26 solved problems (all Easy difficulty)
- Focus on string manipulation, hash tables, and tree traversal
- Includes practical code examples and file I/O patterns

### Decorator Patterns

**decorator_args_kwargs.py**
- Advanced decorator patterns
- Handling *args and **kwargs
- Timing and logging decorators
- Practical examples

**decorator_nnmau.py**
- nnmau decorator pattern
- Use cases and examples

### Modern Python

**dataclass_demo.py**
- Python dataclasses overview
- Field configuration
- Post-init processing
- Comparison with traditional classes

**pytest_demo.py**
- Unit testing with pytest
- Fixtures and parameterization
- Test organization
- Mocking and assertions

## Quick Examples

### Timing Decorator
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"
```

### Dataclass Usage
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"

person = Person("John", 30)
print(person)  # Person(name='John', age=30, email='unknown@example.com')
```

### Pytest Example
```python
import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Running Tests

```bash
# Run all tests
pytest pytest_demo.py -v

# Run specific test
pytest pytest_demo.py::test_name -v

# Run with coverage
pytest --cov=. pytest_demo.py
```

## Best Practices

1. **Use Type Hints**: Improve code clarity and IDE support
2. **Decorators**: DRY principle for cross-cutting concerns
3. **Dataclasses**: Clean data containers with minimal boilerplate
4. **Testing**: Write tests first, use fixtures for setup
5. **Documentation**: Docstrings for all public functions

## References

- [Python Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Dataclasses Guide](https://docs.python.org/3/library/dataclasses.html)
- [Pytest Documentation](https://docs.pytest.org/)
