# Appium2 with Python

The purpose of this Appium2 playground project is to explore the latest version Appium version and see what is needed to
get it all up and running.

## Mobile apps

For Android and IOS we use the lambdatest sample app called [Proverbialfrom](testapps) they are included in this
repository.

## Installation instructions for local setup

Please follow the [installation instructions mac](./documentation/installation_mac.md) before executing tests in
this[requirements.txt](requirements.txt)
framework.

## Local project setup  
Please install all required packages by running ``` pip install -r requirements.txt```  
To run the test locally we make use of the PyTest framework.

## Running tests locally

In order to run tests locally we need to do the following:

1. Start appium server via terminal with ``` appium ```
2. Start emulator you want to run the tests on
3. Run the tests ``` pytest tests/android/test.py ```

## Code formatting and linting

For checking for best practices we use PyLint and for automatically setting up the correct formatting of code we
use [Black](https://black.readthedocs.io/en/stable/index.html)

### PyLint

PyLint checks for best practices and other code smells.  
The configuration of the PyLint is done in [pyproject.toml](./pyproject.toml).

### Black

The configuration of the Black formatter is done in [pyproject.toml](./pyproject.toml).  
Via the command: ⌥⌘L in PyCharm you can configure when to run Black -> I prefer this on save and reformat file.

### Git pre-commit-hook

Via the plugin pre-commit defined in requirements.txt the Black plugin wil automatically run on pre-commit stage.  
This is also defined in the file [.git/hooks/pre-commit](.git/hooks/pre-commit)

```
#!/bin/sh

#Check file formatting and give a warning in the terminal
black --check ./tests/
#Check best practices via PyLint
pylint $(git ls-files '*.py') 

```
