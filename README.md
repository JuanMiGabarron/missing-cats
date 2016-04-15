# Missing Cats
This is a application for search **cats** in a graph of stations and tubes, where the owners check all the stations, if is possible, trying to find their cats.

# Run Application

To run the application you should have python installed 

```
pip install python
```

And just run the following command:

```
python app_missing_cats.py
```
This is a console application, you must put an integer greater than 1 (the number of owners & cats) when the application ask for it and just wait until the application finishes.

# Prints

The application shows severals prints:
* When a owner find his cat
* Total number of cats
* Number of cats found
* Average number of movements required to find a cat
* The owner with the greater number of movements to find his cat

# Tests

We are going to use **tox**, with it we control our virtualenv and tests

To run the tests, simple install tox:

```
pip install tox
```
And run the tox command:

```
tox
```
It will install proper dependencies, execute tests and report results.
