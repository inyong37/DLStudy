# Author      : inyong1020@gmail.com
# Date        : 2020-06-29-Mon.
# Description : Hacker Rank; 30 Days of code; Day 28: RegEx, Patterns, and Intro to Databases.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -
"""
Objective
Today, we're working with regular expressions. Check out the Tutorial tab for learning materials and an instructional video!

Task
Consider a database table, Emails, which has the attributes First Name and Email ID. Given  rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in .

Input Format

The first line contains an integer, , total number of rows in the table.
Each of the  subsequent lines contains  space-separated strings denoting a person's first name and email ID, respectively.

Constraints

Each of the first names consists of lower case letters  only.
Each of the email IDs consists of lower case letters ,  and  only.
The length of the first name is no longer than 20.
The length of the email ID is no longer than 50.
Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

Sample Input

6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
Sample Output

julia
julia
riya
samantha
tanya
"""
# !/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())

    table = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if emailID.endswith('@gmail.com'):
            table.append([firstName, emailID])
    # sorted by name, not email
    for name, email in sorted(table): # same as table.sort(), sorted(table) has return, and table.sort() sorts itself.
        print(name)
