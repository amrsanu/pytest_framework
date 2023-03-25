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
    - pytest
    - pytest -m <marker_name> #To run the specified marker tests
    - pytest -m "<marker1> and/or <marker2>" #To run the multiple marker tests
    - pytest -m "not <marker_name>" #To run all the tests that are not marked with <marker_name>
    - pytest -x To stop execution at first failure
    - pytest -x
    - pytest -x
    - pytest -x
    - pytest -x
    - pytest -s -v -n <number_of_threads>
      - [n] To run using 'pytest-xdist' - Uses parallel execution to run the test functions
      - [s] To show the output of prints to console
      - [v] To run in verbose mode
    - tox To run using the TOX configuration

  - It will run all the test suites decorated using the specified marker.
  - This is auto managing of the test suites.
  - Can define multiple markers for the functions and it kind of groups the test suites under same name.

  - Grouping same markers under a class to eliminate the need to specify the markers for every test function
    - Mark the class with the marker decorator, All the test function inside the class will be added to that marker group.
    - No need to put the same decorator for similar test functions, group them in a same function
    - Classes can also have multiple markers.

## Fixtures

- About

  - Functions used to manage the apps state and dependencies. They provide data for testing and wide range of value types when explicitly called.
  - Runs before/after each test function to which it is applied

- Usage
  - -v: To run in verbose mode
  - -m: To specify the marker
  - -s: To display the prints in the console

- Features

  - Create a python file "conftest.py" to define all the fixtures, pytest will snoop all the fixture
  - No need to inport the fixtures in the modules,
  - Fixtures created in "conftest.py" is accessible to same directory/file and recursive inner firectories/files
  - It will handle the teardown on its own
    - Use yield to return the instance to the calling function.
    - Any statement after the yield will be a teardown
  - Scope
    - package: 
    - module: 
    - class: 
    - function[default]: Every function will get 1 instance
    - session: The complete session will get only one instance

## Reporting

- Generates a document with the details of the run.
  - pytest --html="<html_file_path>", Generates a html document
  - pytest --junitxml="results.xml", Generates a xml document with the details, can be used as plugin in the cloud pipelines like Jenkins.

- Requirements
  - pip install pytest-html

## Handling Test Skips

- To skip the test functions
- Uses marker, @mark.skip(reason="")
- Commands argument to get the Skip prints
  - pytest --env qa -v -rs

## HAndling Expected Test Failures

- To specify the failing test functions that it will fail
- Uses marker, @mark.xfail(reason="")
- Commands argument to get the Skip prints
  - pytest --env qa -v -rx

## Parametrization

- Running the same test with multiple inputs without duplicating the test functions
- Uses marker: pytest.mark.parametrize()
- Using marker parametrization will also be repetitive if you need the same set of data for some other testing function
- Better to use a fixture with 'params'
  - It will run the test function decorated with that fixture for all the params once.

## Fase Testing with Pytest-xdist

- Requirement:
  - pip install pytest-xdist

- Command:
  - pytest -s -v -n <#threads>
  - or
  - pytest -s -v -n auto
  - -n is for number of threads to use to run the test. With 'auto' pytest will try to comup with a optimized number of threads dynamically.
- Will parallelize rhe tests using n threads.
- Good idea is to keep the value of n below the total number of test functions.
  - Don't use huge number of threads, there is a overhead to create and synchronize the threads.
  
## Parallel vs Concurrent

- Normally the tests will not run parallely, they maybe running concurrently by interupting one another.
- To get parallelization we can use 'pytest-xdist' with -n argument

## Unit Testing - White BOX Testing

- We have the source code and have the actual logic implemented.
- Should create a test modume named 'tests' alond the module to be tested
- Mimic the directory and file structure for testing module also
  - To keep track of where the test finction will be for a module

### Test Coverage

- Write tests to cover all the statements of the code

### TOX ???

- Normally its difficult to import the sibling directory and use the modultes to test.
- TOX is generic virtual env management and test commandline tolle to handle above issue and more
- Checks the package works correctly with different version of python
- Can install additional dependency that only the test suite requires.
- Acts as frontend to CI servers

- requirement:
  - pip install tox
  - Configure tox.ini file with the configuration

- TOX will create the new venv for mentioned venv and installs deps. Runs the command provided.
- Can define the pytest.ini configurations in the tox.ini itself.

## Functional Test - Black/Gray Box Testing

- This is not exactly related to any python library (that needs to be tested)
- It runs literally
- Doesnot worry about the logic of the code
- Just verifies the final output for the project as a whole for differnet scenarios.
