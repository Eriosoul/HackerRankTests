"""
Tabulate Module in Python
The tabulate module in Python allows us to create and display data in a tabular format which makes the data look
more readable. It can be used to organize your data to make it more understandable. Below are some of the data
structures in Python which are supported by the tabulate module:

Lists
Dictionary
NumPy Array
Pandas DataFrame
"""

from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Aman", "New Deli", "Male"],["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]
print(tabulate(data))
print("=============================")
print(tabulate(data, headers='firstrow'))
print("=============================")
print(tabulate(data, headers='firstrow', tablefmt='grid'))
print("=============================")
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))