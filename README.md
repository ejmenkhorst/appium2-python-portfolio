# Appium2 with Python

The purpose of this Appium2 playground project is to explore the latest version Appium version and see what is needed to
get it all up and running.

## Mobile apps

For Android and IOS we use the lambdatest sample app called [Proverbialfrom](testapps) they are included in this
repository.

## Installation instructions for local setup

Please follow the [installation instructions mac](./documentation/installation_mac.md) before executing tests in this
framework.

## Local project setup  
Please install all required packages by running ``` pip install -r requirements.txt```  
To run the test locally we make use of the PyTest framework.

## Running tests locally

In order to run tests locally we need to do the following:

1. Start appium server via terminal with ``` appium ```
2. Start emulator you want to run the tests on
3. Run the tests ``` pytest tests/android/test.py ```
