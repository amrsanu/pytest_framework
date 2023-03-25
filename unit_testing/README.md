# Unit Testing - White BOX Testing

- We have the source code and have the actual logic implemented.
- Should create a test modume named 'tests' alond the module to be tested
- Mimic the directory and file structure for testing module also
  - To keep track of where the test finction will be for a module

## Test Coverage

- Write tests to cover all the statements of the code

## TOX ???

- Normally its difficult to import the sibling directory and use the modultes to test.
- TOX is generic virtual env management and test commandline tolle to handle above issue and more
- Checks the package works correctly with different version of python
- Can install additional dependency that only the test suite requires.
- Acts as frontend to CI servers

- requirement:
  - pip install tox
  - Configure tox.ini file with the configuration

- TOX will create the new venv for mentioned venv and installs deps. Runs the command provided.