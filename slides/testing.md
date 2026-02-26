---
layout: default
---

## Engineering model analysis

Before writing a single line of test code, you must understand the physical and logical constraints that govern the system you're testing:

1. **Physical laws are immutable** — Energy cannot be created or destroyed. State constraints must hold. These are domain constraints, not implementation details.

2. **Early error detection** — Understanding the model before coding catches misunderstandings immediately.

3. **Systematic testing** — Constraints and invariants become the foundation for test cases. You derive tests from physics, not guessing.

4. **Clear separation** — Engineering thinking (domain analysis) is distinct from software engineering thinking (test design).

---
layout: default
---

## Engineering model analysis workflow

1. **Study the model** - Understand mathematical definitions, equations, and relationships

2. **Identify constraints**
   - *Bounds:* Valid ranges for each variable
   - *Relationships:* What must always be true about how variables relate
   - *Logical rules:* Decision rules and their preconditions
   - *Invariants:* Properties that must hold regardless of system state or history

3. **Document constraints** - Fill in a constraints table listing all relevant information

Once you've completed this analysis, you have a specification of correct behavior. Your tests will verify that the code respects every one of these constraints.

---
layout: two-cols-header
---

## Components: The Foundation of Testable Code

::left::

- Code must be organized around **testable components** with a clear public interface:
  - Modules, classes, and functions
  - Each with clear, well-defined behaviors

- This is a **fundamental design principle**, not an after-thought:

  - Hard to test code signals design problems (tight coupling between components, unclear responsibilities)
  - Well-structured code is naturally testable (each component has a clear purpose, clear contract that can be verified)

::right::

```
project/
├── src/
│   ├── module_a.py
│   ├── module_b.py
├── tests/
│   ├── test_module_a.py
│   └── test_module_b.py
├── examples/
│   └── validation_scenario.py
└── README.md
```

---
layout: two-cols-header
---

## Two-scale testing strategy

::left::

**Code verification requires:**

1. Automated module tests (`tests/test_*.py`)
  - Unit tests: single function/class
  - Integration tests: multiple components
  - Verify logical correctness (known inputs → expected outputs)
  
2. Validation scripts (*e.g.*, `examples/`)
  - Realistic usage scenarios
  - Multiple modules working together
  - Domain expertise to validate

::right::

```
project/
├── src/
│   ├── module_a.py
│   ├── module_b.py
├── tests/
│   ├── test_module_a.py ← Unit/integration tests
│   └── test_module_b.py ← Unit/integration tests
├── examples/
│   └── validation_scenario.py ← Validation script
└── README.md
```

---
layout: default
---

## Automated module tests

Automated module tests verify, for each module, whether each function, method, and class works as intended.

**Unit testing** builds on four core concepts:

- *Unit* — A small, independent piece of code: a function, method, or class with a clear, single responsibility

- *Behavior* — The observable output or effect a unit produces when given certain inputs. Testing verifies the unit performs exactly as promised

- *Contract* — The explicit promise a function/method makes about what it will do given valid input, and what exception it will raise given invalid input

- *Test double* — A substitute object that replaces an external dependency (database, API, file system, another module) so a unit can be tested in isolation

**Integration tests** follow the same structure but verify that multiple units collaborate correctly.

---
layout: default
---

## Three-step test development

<div v-click="0">

**Step 1: Test definition**
- List all functions and methods in your module and identify what each should do:
  - Normal operation: What does it return with valid input?
  - Edge cases: What happens at boundaries (empty data, zero values, max values)?
  - Error handling: What exception is raised with invalid input?

</div>

<div v-click>

**Step 2: Test implementation**
- Write code for each test case using the **AAA (Arrange, Act, Assert) pattern** 
- Include detailed docstrings
- Use fixtures for reusable test data

</div>

<div v-click>

**Step 3: Test execution, evaluation and refinement**
- Run the tests and generate coverage metrics (line and branch coverage)
- Review test output and plan and add additional tests to meet coverage targets

</div>

---
layout: two-cols-header
---

## The AAA pattern: Arrange, Act, Assert

::left::

Ensuring focused, repeatable, and easy to understand testing:

- **Arrange** — Set up the test environment
  - Create objects and initialize data
  - Prepare everything needed for the test

- **Act** — Execute the specific behavior being tested
  - Call the function/method with test data

- **Assert** — Verify the results
  - Check that output matches expectations
  - Validate state changes

::right::

```python
def test_something():
    """
    Test that [specific behavior] works.
    
    INPUT: What data is created

    EXPECTED OUTPUT: What assertions verify

    CODE PATHS TESTED: Which branches executed
    """
    # Arrange: Set up test data
    obj = MyClass(param1="value")
    
    # Act: Call the method tested
    result = obj.some_method()
    
    # Assert: Verify results
    assert obj.param1 == "value"
    assert result == expected_output
```

---
layout: two-cols-header
---

## Using fixtures for reusable test data

::left::

- **Fixtures** are functions that create and return test data:
  - Defined with `@pytest.fixture` decorator
  - Used by multiple tests without repetition

- Reduce code duplication (DRY principle) by providing shared test data

- Can be session, module, class, or function scoped

::right::

```python
import pytest

@pytest.fixture
def sample_data():
    """Provides test data used by multiple tests."""
    # Create and return test data
    return test_data

def test_something(sample_data):
    """Automatically receives the fixture."""
    result = function_under_test(sample_data)
    assert result == expected

def test_another(sample_data):
    """Another test using the same fixture."""
    output = process(sample_data)
    assert output is not None
```

---
layout: statement
---

## pytest

The standard Python testing framework implementing fixtures, assertions, discovery, and coverage reporting.

https://docs.pytest.org/

---
layout: two-cols-header
---

## Continuous Integration (CI)

::left::

- Automated testing:
  - Automatically run all tests on every code push
  - Catch bugs and issues immediately
  - Ensure code quality before merging

- Faster feedback loops, reduced human error, consistent test execution, repository quality control

::right::

**Example: GitLab CI/CD**

```yaml
stages:
  - test
  - deploy

test:
  stage: test
  script:
    - pytest tests/
    - pytest --cov=src tests/
  
deploy:
  stage: deploy
  script:
    - python -m pip install .
    - deploy_to_production.sh
  only:
    - main
```