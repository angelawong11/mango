# mango

Hello World! This is the start of the mango package.

## Getting Started

### Getting Started on Windows

Installing Python on Windows and getting started with virtualenv.

Reference [Hitchiker's Guide to Python](http://docs.python-guide.org/en/latest/).

1. Follow the python installation instructions
2. If using Windows, virtualenv can be installed as follows:
```
$ # Verify Python version
$ python --version
$ # Verify pip version
$ pip --version
$ # Install virtualenvwrapper for Windows
$ pip install virtualenv
$ pip install virtualenvwrapper-win
```
3. Activate your virtualenv
```
$ # Make a virtualenv for mango the first time
$ mkvirtualenv mango
$ # For the first and subsequent times, 'workon' your virtualenv
$ workon mango
```
Visit the Hitchiker's for more detailed general instructions about using
Python and Windows.

### Getting started with mango

Assuming your virtualenv is created.
1. `$ workon mango`
1. `$ pip install -r dev_requirements.txt`

## Running tests

`$ python setup.py test`
