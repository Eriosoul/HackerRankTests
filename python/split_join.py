"""
>>> a = "this is a string"
>>> a = a.split(" ")  # is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.
"""

def split_and_join(line):
    # write your code here
    a_split_line = line.split(" ")
    b_join_line = "-".join(a_split_line)
    return b_join_line

if __name__ == '__main__':
    line = "Esto es un juego feliz"
    result = split_and_join(line)
    print(result)