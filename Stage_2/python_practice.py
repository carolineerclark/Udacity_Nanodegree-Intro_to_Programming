# Problems taken from http://codingbat.com/python/Warmup-1

# Problem 1: sum_double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b
  
# Problem 2: makes10
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
    if a + b == 10 or a == 10 or b == 10:
        return True
    else:
        return False
      
# Problem 3: diff21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n
