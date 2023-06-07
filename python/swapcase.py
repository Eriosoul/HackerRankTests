"""
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string s
"""

def swap_case(s):
    palabra = s.swapcase()
    return palabra

if __name__ == '__main__':
    s = "Pythonist 2"
    result = swap_case(s)
    print(result)