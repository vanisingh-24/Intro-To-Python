# Given a full name, your task is to capitalize the name appropriately.

def capitalize(s):
  return ' '.join(i.capitalize() for i in s.split(' '))

# Driver Code
s = input()
print(capitalize(s))

# OR using buil-in function capwords()

import string

def capitalize(s):
  return string.capwords(s, ' ')

# Driver Code
s = input()
print(capitalize(s))