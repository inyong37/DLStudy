# Author      : inyong1020@gmail.com
# Date        : 2020-06-27-Sat.
# Description : Hacker Rank; 30 Days of code; Day 25: Running Time and Complexity.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -
# Reference   : https://www.hackerrank.com/challenges/30-running-time-and-complexity/forum/comments/495184
"""
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.
 """
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from math import ceil, sqrt


def check(integer):
    if integer <= 1:
        return print('Not prime')
    if integer is 2:
        return print('Prime')
    if not integer % 2:
        return print('Not prime')
    for i in range(3, ceil(sqrt(integer))+1, 2):
        if integer % i == 0:
            return print('Not prime')
    return print('Prime')


n = int(sys.stdin.readline())
for _ in range(n):
    check(int(sys.stdin.readline()))

