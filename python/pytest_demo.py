# pytest_demo.py
"""
Complete Pytest Demo - Covering All Important Skills
=====================================================

Run tests with: pytest pytest_demo.py -v
Run with coverage: pytest pytest_demo.py --cov=. -v
Run specific test: pytest pytest_demo.py::test_basic_assertion -v
Run by marker: pytest pytest_demo.py -m slow -v

Table of Contents:
1. Basic Assertions
2. Fixtures (setup/teardown)
3. Parametrized Tests
4. Mocking with unittest.mock
5. Exception Testing
6. Markers (skip, xfail, custom)
7. Fixture Scopes (function, class, module, session)
8. Conftest.py patterns
9. Monkeypatching
10. Temporary Files and Directories
11. Capturing stdout/stderr
12. Testing Classes
13. Async Testing
"""

import pytest
import os
import tempfile
import json
from unittest.mock import Mock, MagicMock, patch, call
from typing import List, Dict, Any
from dataclasses import dataclass


# =============================================================================
# SAMPLE CODE TO TEST (normally in separate files)
# =============================================================================

def add(a: int, b: int) -> int:
    """Simple addition function"""
    return a + b


def divide(a: float, b: float) -> float:
    """Division with zero check"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """Simulates an API call - we'll mock this"""
    # In real code, this would call an external API
    import requests
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()


def process_user(user_id: int) -> str:
    """Process user data - depends on fetch_user_data"""
    data = fetch_user_data(user_id)
    return f"Hello, {data['name']}! You have {data['points']} points."


def read_config(filepath: str) -> Dict:
    """Read JSON config file"""
    with open(filepath, 'r') as f:
        return json.load(f)


def get_environment_variable(name: str) -> str:
    """Get environment variable"""
    value = os.environ.get(name)
    if value is None:
        raise KeyError(f"Environment variable {name} not found")
    return value


@dataclass
class User:
    """User dataclass for testing"""
    id: int
    name: str
    email: str
    
    def greet(self) -> str:
        return f"Hello, {self.name}!"
    
    def update_email(self, new_email: str) -> None:
        if "@" not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email


class Calculator:
    """Calculator class for testing"""
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def clear_history(self) -> None:
        self.history = []


class DatabaseConnection:
    """Simulates database connection for testing"""
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self) -> None:
        print(f"Connecting to {self.connection_string}...")
        self.connected = True
    
    def disconnect(self) -> None:
        print("Disconnecting...")
        self.connected = False
    
    def query(self, sql: str) -> List[Dict]:
        if not self.connected:
            raise RuntimeError("Not connected to database")
        return [{"id": 1, "name": "test"}]


# =============================================================================
# 1. BASIC ASSERTIONS
# =============================================================================

def test_basic_assertion():
    """Basic equality assertion"""
    assert add(2, 3) == 5


def test_assertion_with_message():
    """Assertion with custom error message"""
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"


def test_multiple_assertions():
    """Multiple assertions in one test"""
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(100, 200) == 300


def test_approximate_equality():
    """Testing floating point with approximate equality"""
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)
    assert result == pytest.approx(0.3, rel=1e-9)  # relative tolerance
    assert result == pytest.approx(0.3, abs=1e-10)  # absolute tolerance


def test_list_and_dict_assertions():
    """Testing collections"""
    # List assertions
    assert [1, 2, 3] == [1, 2, 3]
    assert 2 in [1, 2, 3]
    assert len([1, 2, 3]) == 3
    
    # Dict assertions
    data = {"name": "Alice", "age": 30}
    assert data["name"] == "Alice"
    assert "age" in data
    assert data == {"name": "Alice", "age": 30}


def test_string_assertions():
    """Testing strings"""
    message = "Hello, World!"
    assert "Hello" in message
    assert message.startswith("Hello")
    assert message.endswith("!")
    assert len(message) == 13


def test_boolean_assertions():
    """Testing boolean values"""
    assert True
    assert not False
    assert bool(1)
    assert not bool(0)
    assert bool([1, 2, 3])  # non-empty list is truthy
    assert not bool([])  # empty list is falsy


# =============================================================================
# 2. FIXTURES (Setup/Teardown)
# =============================================================================

@pytest.fixture
def sample_user():
    """Basic fixture - creates a User for testing"""
    return User(id=1, name="Alice", email="alice@example.com")


@pytest.fixture
def calculator():
    """Fixture that returns a Calculator instance"""
    return Calculator()


@pytest.fixture
def sample_data():
    """Fixture with setup and teardown using yield"""
    # SETUP: Code before yield runs before the test
    print("\n[SETUP] Creating sample data...")
    data = {"users": [1, 2, 3], "count": 3}
    
    yield data  # This is what the test receives
    
    # TEARDOWN: Code after yield runs after the test
    print("\n[TEARDOWN] Cleaning up sample data...")
    data.clear()


@pytest.fixture
def temp_config_file():
    """Fixture that creates a temporary file"""
    # Create temp file
    config = {"debug": True, "version": "1.0.0"}
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(config, f)
        filepath = f.name
    
    yield filepath
    
    # Cleanup: remove temp file
    if os.path.exists(filepath):
        os.remove(filepath)


@pytest.fixture
def database():
    """Fixture with setup and teardown for database connection"""
    # Setup
    db = DatabaseConnection("localhost:5432/test")
    db.connect()
    
    yield db
    
    # Teardown
    db.disconnect()


def test_with_fixture(sample_user):
    """Test that uses a fixture"""
    assert sample_user.name == "Alice"
    assert sample_user.greet() == "Hello, Alice!"


def test_calculator_fixture(calculator):
    """Test using calculator fixture"""
    assert calculator.add(2, 3) == 5
    assert len(calculator.history) == 1


def test_with_yield_fixture(sample_data):
    """Test that uses a fixture with setup/teardown"""
    assert sample_data["count"] == 3
    assert len(sample_data["users"]) == 3


def test_temp_file_fixture(temp_config_file):
    """Test using temporary file fixture"""
    config = read_config(temp_config_file)
    assert config["debug"] is True
    assert config["version"] == "1.0.0"


def test_database_fixture(database):
    """Test using database fixture"""
    assert database.connected is True
    result = database.query("SELECT * FROM users")
    assert len(result) > 0


# =============================================================================
# 3. PARAMETRIZED TESTS
# =============================================================================

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (-5, -3, -8),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test - runs once for each set of parameters"""
    assert add(a, b) == expected


@pytest.mark.parametrize("input_str, expected_len", [
    ("hello", 5),
    ("", 0),
    ("pytest is awesome", 17),
])
def test_string_length_parametrized(input_str, expected_len):
    """Parametrized test for string operations"""
    assert len(input_str) == expected_len


@pytest.mark.parametrize("dividend, divisor, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (7, 2, 3.5),
    (0, 5, 0.0),
])
def test_divide_parametrized(dividend, divisor, expected):
    """Parametrized division tests"""
    assert divide(dividend, divisor) == expected


# Multiple parametrize decorators create a cartesian product
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_cartesian_product(x, y):
    """This runs 4 times: (1,10), (1,20), (2,10), (2,20)"""
    assert x * y in [10, 20, 40]


# Parametrize with IDs for better test names
@pytest.mark.parametrize("email, valid", [
    pytest.param("user@example.com", True, id="valid_email"),
    pytest.param("invalid-email", False, id="missing_at_symbol"),
    pytest.param("@example.com", False, id="missing_username"),
], ids=str)
def test_email_validation(email, valid):
    """Parametrized test with custom IDs"""
    result = "@" in email and email.index("@") > 0
    assert result == valid


# =============================================================================
# 4. MOCKING WITH UNITTEST.MOCK
# =============================================================================

def test_basic_mock():
    """Basic Mock object usage"""
    mock_obj = Mock()
    
    # Mock can have any attribute or method
    mock_obj.some_method.return_value = 42
    assert mock_obj.some_method() == 42
    
    # Verify the mock was called
    mock_obj.some_method.assert_called_once()


def test_mock_with_side_effect():
    """Mock with side effects"""
    mock_func = Mock()
    
    # Side effect: different return values for each call
    mock_func.side_effect = [1, 2, 3]
    assert mock_func() == 1
    assert mock_func() == 2
    assert mock_func() == 3
    
    # Side effect: raise an exception
    mock_error = Mock(side_effect=ValueError("Oops!"))
    with pytest.raises(ValueError, match="Oops!"):
        mock_error()


def test_magic_mock():
    """MagicMock - Mock with magic methods pre-configured"""
    magic = MagicMock()
    
    # MagicMock supports magic methods out of the box
    magic.__len__.return_value = 5
    assert len(magic) == 5
    
    magic.__getitem__.return_value = "item"
    assert magic[0] == "item"


@patch('pytest_demo.fetch_user_data')
def test_patch_decorator(mock_fetch):
    """Using @patch decorator to mock a function"""
    # Configure the mock
    mock_fetch.return_value = {"name": "Bob", "points": 100}
    
    # Call the function that uses fetch_user_data
    result = process_user(123)
    
    # Assertions
    assert result == "Hello, Bob! You have 100 points."
    mock_fetch.assert_called_once_with(123)


def test_patch_context_manager():
    """Using patch as a context manager"""
    with patch('pytest_demo.fetch_user_data') as mock_fetch:
        mock_fetch.return_value = {"name": "Charlie", "points": 50}
        
        result = process_user(456)
        
        assert result == "Hello, Charlie! You have 50 points."
        mock_fetch.assert_called_with(456)


def test_patch_object():
    """Patching an object's method"""
    user = User(id=1, name="Test", email="test@example.com")
    
    with patch.object(user, 'greet', return_value="Mocked greeting!"):
        assert user.greet() == "Mocked greeting!"


def test_mock_call_args():
    """Inspecting mock call arguments"""
    mock_func = Mock()
    
    mock_func(1, 2, key="value")
    mock_func(3, 4, key="other")
    
    # Check call count
    assert mock_func.call_count == 2
    
    # Check all calls
    mock_func.assert_has_calls([
        call(1, 2, key="value"),
        call(3, 4, key="other"),
    ])
    
    # Check last call
    mock_func.assert_called_with(3, 4, key="other")
    
    # Access call arguments
    args, kwargs = mock_func.call_args
    assert args == (3, 4)
    assert kwargs == {"key": "other"}


def test_mock_return_value_chain():
    """Mocking chained method calls"""
    mock_api = MagicMock()
    
    # Mock: api.users.get(1).json()
    mock_api.users.get.return_value.json.return_value = {"id": 1, "name": "Alice"}
    
    result = mock_api.users.get(1).json()
    assert result["name"] == "Alice"


@patch.multiple('pytest_demo', 
                fetch_user_data=Mock(return_value={"name": "Multi", "points": 99}))
def test_patch_multiple():
    """Patching multiple objects at once"""
    result = process_user(1)
    assert "Multi" in result


# =============================================================================
# 5. EXCEPTION TESTING
# =============================================================================

def test_raises_exception():
    """Test that a function raises an exception"""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_raises_with_message():
    """Test exception with specific message"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_raises_and_inspect():
    """Capture and inspect the exception"""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    
    # Inspect the exception
    assert "zero" in str(exc_info.value)
    assert exc_info.type == ValueError


def test_exception_in_class():
    """Test exception in class method"""
    user = User(id=1, name="Test", email="test@example.com")
    
    with pytest.raises(ValueError, match="Invalid email"):
        user.update_email("invalid-email")


def test_no_exception():
    """Verify no exception is raised"""
    # This should not raise
    result = divide(10, 2)
    assert result == 5.0


# =============================================================================
# 6. MARKERS (skip, xfail, custom)
# =============================================================================

@pytest.mark.skip(reason="Skipping this test for demonstration")
def test_skip_always():
    """This test is always skipped"""
    assert False  # Would fail if not skipped


@pytest.mark.skipif(os.name == 'nt', reason="Skip on Windows")
def test_skip_on_windows():
    """This test is skipped on Windows"""
    assert True


@pytest.mark.xfail(reason="This feature is not implemented yet")
def test_expected_failure():
    """This test is expected to fail"""
    assert 1 == 2  # Will fail, but marked as xfail


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_xfail_specific_exception():
    """Expected to fail with specific exception"""
    result = 1 / 0


# Custom markers (define in pytest.ini or pyproject.toml)
@pytest.mark.slow
def test_marked_as_slow():
    """Custom marker for slow tests - run with: pytest -m slow"""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.integration
def test_marked_as_integration():
    """Custom marker for integration tests"""
    assert True


# =============================================================================
# 7. FIXTURE SCOPES
# =============================================================================

@pytest.fixture(scope="function")  # Default - runs for each test function
def function_scoped_fixture():
    """Created fresh for each test function"""
    print("\n  [function scope] Creating fixture")
    return {"calls": 0}


@pytest.fixture(scope="class")
def class_scoped_fixture():
    """Created once per test class"""
    print("\n  [class scope] Creating fixture")
    return {"calls": 0}


@pytest.fixture(scope="module")
def module_scoped_fixture():
    """Created once per test module"""
    print("\n  [module scope] Creating fixture")
    return {"calls": 0}


@pytest.fixture(scope="session")
def session_scoped_fixture():
    """Created once per test session"""
    print("\n  [session scope] Creating fixture")
    return {"calls": 0}


class TestFixtureScopes:
    """Test class demonstrating fixture scopes"""
    
    def test_first(self, function_scoped_fixture, class_scoped_fixture):
        function_scoped_fixture["calls"] += 1
        class_scoped_fixture["calls"] += 1
        assert function_scoped_fixture["calls"] == 1
        # class_scoped_fixture persists across tests in this class
    
    def test_second(self, function_scoped_fixture, class_scoped_fixture):
        function_scoped_fixture["calls"] += 1
        class_scoped_fixture["calls"] += 1
        assert function_scoped_fixture["calls"] == 1  # Fresh fixture
        assert class_scoped_fixture["calls"] == 2  # Same fixture, incremented


# =============================================================================
# 8. FIXTURE DEPENDENCIES & AUTOUSE
# =============================================================================

@pytest.fixture
def base_config():
    """Base configuration fixture"""
    return {"debug": False, "version": "1.0"}


@pytest.fixture
def extended_config(base_config):
    """Fixture that depends on another fixture"""
    base_config["extra_setting"] = True
    return base_config


def test_fixture_dependency(extended_config):
    """Test using fixture with dependencies"""
    assert extended_config["debug"] is False
    assert extended_config["extra_setting"] is True


@pytest.fixture(autouse=True)
def setup_for_all_tests():
    """Autouse fixture - runs automatically for all tests"""
    print("\n  [autouse] Running before test...")
    yield
    print("\n  [autouse] Running after test...")


# =============================================================================
# 9. MONKEYPATCHING
# =============================================================================

def test_monkeypatch_env_variable(monkeypatch):
    """Monkeypatch environment variables"""
    # Set an environment variable
    monkeypatch.setenv("MY_API_KEY", "secret123")
    
    result = get_environment_variable("MY_API_KEY")
    assert result == "secret123"


def test_monkeypatch_delenv(monkeypatch):
    """Monkeypatch to delete environment variable"""
    # First set it
    monkeypatch.setenv("TEMP_VAR", "value")
    assert os.environ.get("TEMP_VAR") == "value"
    
    # Then delete it
    monkeypatch.delenv("TEMP_VAR")
    assert os.environ.get("TEMP_VAR") is None


def test_monkeypatch_attribute(monkeypatch):
    """Monkeypatch an object attribute"""
    user = User(id=1, name="Original", email="original@example.com")
    
    # Change the name attribute
    monkeypatch.setattr(user, "name", "Patched")
    
    assert user.name == "Patched"
    assert user.greet() == "Hello, Patched!"


def test_monkeypatch_function(monkeypatch):
    """Monkeypatch a function"""
    def mock_fetch(user_id):
        return {"name": "Monkeypatched", "points": 999}
    
    # Replace the function
    monkeypatch.setattr('pytest_demo.fetch_user_data', mock_fetch)
    
    result = process_user(1)
    assert "Monkeypatched" in result
    assert "999" in result


def test_monkeypatch_dict(monkeypatch):
    """Monkeypatch dictionary items"""
    config = {"setting1": "original", "setting2": "value2"}
    
    # Modify dict item
    monkeypatch.setitem(config, "setting1", "modified")
    assert config["setting1"] == "modified"
    
    # Delete dict item
    monkeypatch.delitem(config, "setting2")
    assert "setting2" not in config


# =============================================================================
# 10. TEMPORARY FILES AND DIRECTORIES
# =============================================================================

def test_tmp_path(tmp_path):
    """Built-in tmp_path fixture for temporary directory"""
    # tmp_path is a pathlib.Path object
    temp_file = tmp_path / "test_file.txt"
    temp_file.write_text("Hello, pytest!")
    
    assert temp_file.exists()
    assert temp_file.read_text() == "Hello, pytest!"
    # Automatically cleaned up after test


def test_tmp_path_factory(tmp_path_factory):
    """tmp_path_factory for creating multiple temp directories"""
    # Create named temporary directories
    dir1 = tmp_path_factory.mktemp("data1")
    dir2 = tmp_path_factory.mktemp("data2")
    
    (dir1 / "file1.txt").write_text("content1")
    (dir2 / "file2.txt").write_text("content2")
    
    assert (dir1 / "file1.txt").exists()
    assert (dir2 / "file2.txt").exists()


def test_tmpdir(tmpdir):
    """Legacy tmpdir fixture (py.path.local object)"""
    # tmpdir is a py.path.local object
    temp_file = tmpdir.join("test.txt")
    temp_file.write("content")
    
    assert temp_file.read() == "content"


# =============================================================================
# 11. CAPTURING STDOUT/STDERR
# =============================================================================

def test_capture_stdout(capsys):
    """Capture and test stdout output"""
    print("Hello, stdout!")
    print("Second line")
    
    captured = capsys.readouterr()
    
    assert "Hello, stdout!" in captured.out
    assert "Second line" in captured.out
    assert captured.err == ""  # No stderr


def test_capture_stderr(capsys):
    """Capture stderr output"""
    import sys
    print("Error message!", file=sys.stderr)
    
    captured = capsys.readouterr()
    
    assert "Error message!" in captured.err


def test_capture_with_db_fixture(capsys, database):
    """Capture output from fixture"""
    # database fixture prints "Connecting..."
    captured = capsys.readouterr()
    
    assert "Connecting" in captured.out


def test_capfd(capfd):
    """capfd captures at file descriptor level (includes subprocesses)"""
    print("File descriptor output")
    
    captured = capfd.readouterr()
    assert "File descriptor output" in captured.out


def test_caplog(caplog):
    """Capture log messages"""
    import logging
    
    logger = logging.getLogger(__name__)
    logger.warning("This is a warning")
    logger.error("This is an error")
    
    assert "This is a warning" in caplog.text
    assert "This is an error" in caplog.text
    
    # Check log records
    assert len(caplog.records) == 2
    assert caplog.records[0].levelname == "WARNING"
    assert caplog.records[1].levelname == "ERROR"


# =============================================================================
# 12. TESTING CLASSES
# =============================================================================

class TestCalculator:
    """Test class for Calculator - groups related tests"""
    
    @pytest.fixture(autouse=True)
    def setup_calculator(self):
        """Setup fixture that runs for each test method"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test add method"""
        assert self.calc.add(2, 3) == 5
    
    def test_multiply(self):
        """Test multiply method"""
        assert self.calc.multiply(4, 5) == 20
    
    def test_history(self):
        """Test history tracking"""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        
        assert len(self.calc.history) == 2
        assert "1 + 2 = 3" in self.calc.history
        assert "3 * 4 = 12" in self.calc.history
    
    def test_clear_history(self):
        """Test clearing history"""
        self.calc.add(1, 1)
        self.calc.clear_history()
        
        assert len(self.calc.history) == 0


class TestUser:
    """Test class for User dataclass"""
    
    @pytest.fixture
    def user(self):
        return User(id=1, name="TestUser", email="test@example.com")
    
    def test_greet(self, user):
        assert user.greet() == "Hello, TestUser!"
    
    def test_update_email_valid(self, user):
        user.update_email("new@example.com")
        assert user.email == "new@example.com"
    
    def test_update_email_invalid(self, user):
        with pytest.raises(ValueError):
            user.update_email("invalid-email")


# =============================================================================
# 13. ASYNC TESTING (requires pytest-asyncio)
# =============================================================================

# Uncomment if you have pytest-asyncio installed
# import asyncio
# 
# async def async_fetch_data(url: str) -> Dict:
#     """Async function to test"""
#     await asyncio.sleep(0.1)  # Simulate async operation
#     return {"url": url, "status": "success"}
# 
# 
# @pytest.mark.asyncio
# async def test_async_function():
#     """Test async function"""
#     result = await async_fetch_data("https://example.com")
#     assert result["status"] == "success"
# 
# 
# @pytest.mark.asyncio
# async def test_async_with_mock():
#     """Test async function with mock"""
#     with patch('pytest_demo.async_fetch_data') as mock_fetch:
#         mock_fetch.return_value = {"url": "mocked", "status": "mocked"}
#         
#         result = await async_fetch_data("any")
#         assert result["status"] == "mocked"


# =============================================================================
# 14. BONUS: REQUEST FIXTURE (access test metadata)
# =============================================================================

def test_request_fixture(request):
    """Access test metadata via request fixture"""
    # Get current test name
    test_name = request.node.name
    assert test_name == "test_request_fixture"
    
    # Get test module
    module = request.module
    assert module.__name__ == "pytest_demo"


# =============================================================================
# 15. BONUS: DOCTEST INTEGRATION
# =============================================================================

def factorial(n: int) -> int:
    """
    Calculate factorial of n.
    
    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(3)
        6
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# =============================================================================
# SUMMARY: PYTEST CHEATSHEET
# =============================================================================
"""
QUICK REFERENCE:
================

RUNNING TESTS:
    pytest                          # Run all tests
    pytest -v                       # Verbose output
    pytest -vv                      # More verbose
    pytest test_file.py             # Run specific file
    pytest test_file.py::test_func  # Run specific test
    pytest -k "add"                 # Run tests matching name
    pytest -m slow                  # Run tests with marker
    pytest -x                       # Stop on first failure
    pytest --lf                     # Run last failed tests
    pytest --ff                     # Run failed tests first
    pytest -n auto                  # Parallel execution (pytest-xdist)
    pytest --cov=src                # Coverage report (pytest-cov)

ASSERTIONS:
    assert x == y                   # Equality
    assert x != y                   # Inequality
    assert x in collection          # Membership
    assert x is None                # Identity
    assert x == pytest.approx(y)    # Float comparison
    
FIXTURES:
    @pytest.fixture                 # Basic fixture
    @pytest.fixture(scope="...")    # function/class/module/session
    @pytest.fixture(autouse=True)   # Auto-apply fixture
    yield value                     # Setup/teardown pattern

MARKERS:
    @pytest.mark.skip               # Skip test
    @pytest.mark.skipif(cond)       # Conditional skip
    @pytest.mark.xfail              # Expected failure
    @pytest.mark.parametrize        # Parametrized tests
    @pytest.mark.custom_name        # Custom markers

MOCKING:
    Mock()                          # Basic mock
    MagicMock()                     # Mock with magic methods
    @patch('module.function')       # Patch decorator
    patch.object(obj, 'method')     # Patch object method
    mock.return_value = x           # Set return value
    mock.side_effect = [1, 2]       # Multiple returns
    mock.assert_called_once()       # Verify calls

BUILT-IN FIXTURES:
    tmp_path                        # Temporary directory (pathlib.Path)
    tmp_path_factory                # Create multiple temp dirs
    capsys                          # Capture stdout/stderr
    caplog                          # Capture logging
    monkeypatch                     # Dynamic patching
    request                         # Test metadata
"""


if __name__ == "__main__":
    # Run tests programmatically
    pytest.main([__file__, "-v"])
