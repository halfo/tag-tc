# Tag TopCoder

> It's rough, it's messy, it's untidy, it's slow, it's not how you expect it to be, but still, it works!!

Tag TopCoder is a script that finds topcoder problems by user-defined tags/categories.

The problem with topcoder's category is that it's too generic. Suppose, you want to find problems related to Network flow, but there's no category for it. The only way to find them is to look at every  problems under "Graph Theory" category. And there are thousands of them.

But, it is highly probable that a Network flow related problem's editorial page would contain the word "flow" atleast once. So, this script looks into every editorial page, search for given keywords (in this case - "flow") and list those pages where it has found a match. 


# Usage

- Provide username (your TC handle). If you leave it blank, you would be asked after you run the script.

```python
username = ""
```
- Provide password (your TC password). If you leave it blank, you would be asked after you run the script.

```python
password = ""
```

- List of keywords. For example, if you are looking for problems related to probability, the list can be like following,

```python
keywords = ["probability", "expected value", "expectation"]
```

-  Maximum number of problems you want to find

```python
limit = 10000 
```

- The script is written in python. So, you must have [Python](https://www.python.org/). Also there are some dependencieds:
	1. [Selenium](https://selenium-python.readthedocs.org/installation.html)
	2. [html2text](http://www.mbayer.de/html2text/) 

This script takes around ~40 minutes to run and create a html page containing links of the editorial pages that contains atleast one of the given keywords.


# About

Developed by [Hasib Billah](https://github.com/halfo/).</br>
Released under the [GNU GPL v2.0](https://en.wikipedia.org/wiki/GNU_General_Public_License#Version_2) license.
