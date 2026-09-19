#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

print(minOperations(4))   # 4
print(minOperations(12))  # 7
print(minOperations(9))   # 6
print(minOperations(1))   # 0
print(minOperations(0))   # 0
print(minOperations(17))  