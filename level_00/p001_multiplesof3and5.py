""" 
https://projecteuler.net/problem=1
Problem 001

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution(N):
    result = 0
    for i in range(0, N):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

# The above code is straightforward. However, it can be simplified using
# a generator expresssion:

def solutionGen(N):
    return sum(i for i in range(0, N) if i % 3 == 0 or i % 5 == 0)

# More on generators:
# https://wiki.python.org/moin/Generators
# https://www.python.org/dev/peps/pep-0289/
