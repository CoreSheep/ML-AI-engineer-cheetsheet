# Dataclass Demo - Core Concepts
"""
@dataclass is a decorator that automatically generates boilerplate code for classes.

It auto-generates:
- __init__()      : Constructor
- __repr__()      : String representation
- __eq__()        : Equality comparison (==)

Why use dataclass?
- Less boilerplate code
- More readable
- Type hints built-in
"""

from dataclasses import dataclass


# =============================================================================
# WITHOUT DATACLASS (Traditional Way) - Lots of Boilerplate!
# =============================================================================

class PersonTraditional:
    """Traditional class - you write EVERYTHING manually"""
    
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"PersonTraditional(name='{self.name}', age={self.age}, email='{self.email}')"
    
    def __eq__(self, other):
        if not isinstance(other, PersonTraditional):
            return False
        return self.name == other.name and self.age == other.age and self.email == other.email


# =============================================================================
# WITH DATACLASS - Clean and Simple!
# =============================================================================

@dataclass
class Person:
    """Dataclass - all boilerplate is AUTO-GENERATED!"""
    name: str
    age: int
    email: str


# =============================================================================
# __POST_INIT__ - Run code AFTER __init__ completes
# =============================================================================
"""
__post_init__ is a special method that runs AFTER the auto-generated __init__.

Use cases:
- Validation (check if values are valid)
- Computed fields (derive values from other fields)
- Data transformation (normalize data)
"""

@dataclass
class Employee:
    """Dataclass with __post_init__ for validation and computed fields"""
    first_name: str
    last_name: str
    age: int
    salary: float
    
    # These will be set in __post_init__ (not in constructor)
    full_name: str = ""       # Computed field (with default value) or full_name: str = field(init=False)
    is_senior: bool = False   # Computed field (with default value) or is_senior: bool = field(init=False)
    
    def __post_init__(self):
        """
        This runs AFTER __init__ completes.
        
        Execution order:
        1. __init__ sets: first_name, last_name, age, salary
        2. __post_init__ runs: computes full_name, is_senior, validates age
        """
        # Computed field: combine first and last name
        self.full_name = f"{self.first_name} {self.last_name}"
        
        # Computed field: determine seniority
        self.is_senior = self.age >= 40
        
        # Validation: age must be positive
        if self.age < 0:
            raise ValueError(f"Age cannot be negative: {self.age}")
        
        # Validation: salary must be positive
        if self.salary < 0:
            raise ValueError(f"Salary cannot be negative: {self.salary}")


@dataclass
class Rectangle:
    """Another __post_init__ example: computed properties"""
    width: float
    height: float
    
    # Computed fields
    area: float = 0.0
    perimeter: float = 0.0
    
    def __post_init__(self):
        """Calculate area and perimeter from width and height"""
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


# =============================================================================
# DEMO: Let's see them in action!
# =============================================================================

if __name__ == "__main__":
    
    print("=" * 60)
    print("DATACLASS CORE CONCEPTS DEMO")
    print("=" * 60)
    
    # 1. Creating instances (same syntax for both)
    print("\n1. Creating instances:")
    
    traditional = PersonTraditional("Alice", 30, "alice@example.com")
    dataclass_person = Person("Alice", 30, "alice@example.com")
    
    print(f"   Traditional: {traditional}")
    print(f"   Dataclass:   {dataclass_person}")
    
    # 2. Auto-generated __repr__ (nice string output)
    print("\n2. __repr__ (string representation):")
    print(f"   {dataclass_person}")
    # Output: Person(name='Alice', age=30, email='alice@example.com')
    
    # 3. Auto-generated __eq__ (equality comparison)
    print("\n3. __eq__ (equality comparison):")
    
    person1 = Person("Bob", 25, "bob@example.com")
    person2 = Person("Bob", 25, "bob@example.com")
    person3 = Person("Charlie", 35, "charlie@example.com")
    
    print(f"   person1 == person2: {person1 == person2}")  # True (same values)
    print(f"   person1 == person3: {person1 == person3}")  # False (different values)
    
    # 4. Accessing attributes
    print("\n4. Accessing attributes:")
    print(f"   Name: {dataclass_person.name}")
    print(f"   Age:  {dataclass_person.age}")
    print(f"   Email: {dataclass_person.email}")
    
    # 5. Modifying attributes (mutable by default)
    print("\n5. Modifying attributes:")
    dataclass_person.age = 31
    print(f"   After birthday: {dataclass_person}")
    
    # =================================================================
    # __POST_INIT__ DEMO
    # =================================================================
    print("\n" + "=" * 60)
    print("__POST_INIT__ DEMO")
    print("=" * 60)
    
    # 6. Employee with computed fields
    print("\n6. Employee with __post_init__ (computed fields):")
    emp = Employee("John", "Doe", 45, 75000.0)
    print(f"   Employee: {emp}")
    print(f"   Full Name: {emp.full_name}")      # Computed from first + last
    print(f"   Is Senior: {emp.is_senior}")      # Computed from age >= 40
    
    # 7. Validation in __post_init__
    print("\n7. Validation in __post_init__:")
    try:
        bad_emp = Employee("Bad", "Person", -5, 50000.0)  # Negative age!
    except ValueError as e:
        print(f"   Caught error: {e}")
    
    # 8. Rectangle with computed area and perimeter
    print("\n8. Rectangle with computed properties:")
    rect = Rectangle(10.0, 5.0)
    print(f"   Rectangle: {rect}")
    print(f"   Area: {rect.area}")               # Computed: 10 * 5 = 50
    print(f"   Perimeter: {rect.perimeter}")     # Computed: 2*(10+5) = 30
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("  1. @dataclass saves you from writing __init__, __repr__, __eq__")
    print("  2. __post_init__ runs AFTER __init__ for:")
    print("     - Computed fields (derive from other fields)")
    print("     - Validation (check if values are valid)")
    print("     - Data transformation")
    print("=" * 60)


# =============================================================================
# QUICK COMPARISON
# =============================================================================
"""
TRADITIONAL CLASS (15+ lines):
    class Person:
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
        
        def __repr__(self):
            return f"Person(name='{self.name}', ...)"
        
        def __eq__(self, other):
            return self.name == other.name and ...

DATACLASS (4 lines):
    @dataclass
    class Person:
        name: str
        age: int
        email: str

Same functionality, 75% less code! 🎉
"""
