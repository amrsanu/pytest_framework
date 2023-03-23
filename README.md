# Python PYTEST for Test Automation

## About Pytest

- Test framework based on Python language
- Easy to write, execute and generate test reports, Auto detect tests, Grouping/ Mrking Tests, Uses Python assert keyword, can run tests written in unittest or nose, CI/CD integration, Good features - Fixtures, Parameterize, etc.
- Different types and level of testing
- Like - Unit Testing, backend, Gui Testing...
- Other Python testing framework: unittest and nose

## Class, File & Function naming convention

- Classes: Test*
- Files: test_*.py / *_test.py for pytest to look for all the test scripts
- Functions: def test_*()

## Suggestions

- Use "pytest.ini" to customize the naming conventions and other pytest properties.
  - Its not a good idea to manage test manually.
- Try to organise the tests in directories > files > classes > functions. 


## Documentation

- Markers
  - Use mark from pytest to enable selecting a set of test suites to run
  - Define marker using: @mark.<marker_name>
  - Command:
    - pytest -m <marker_name> #To run the specified marker tests
    - pytest -m "<marker1> and/or <marker2>" #To run the multiple marker tests
    - pytest -m "not <marker_name>" #To run all the tests that are not marked with <marker_name>

  - It will run all the test suites decorated using the specified marker.
  - This is auto managing of the test suites.
  - Can define multiple markers for the functions and it kind of groups the test suites under same name.
