#!/usr/bin/env python3
s = input("Please enter s string: ")
z = s[::-1]
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
