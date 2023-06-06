"""
Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to 2, 5 print Not Weird
If n is even and in the inclusive range of  to 6, 20 print Weird
If n is even and greater than 20, print Not Weird
"""

if __name__ == '__main__':
    n = int(input().strip())
    assert (n >= 0 and n <= 100)
    if n % 2 != 0 or (n >= 6 and n <= 20 and n % 2 == 0):
        print("Weird")
    elif n % 2 == 0 and ((n >= 2 and n <= 5) or n > 20):
        print("Not Weird")