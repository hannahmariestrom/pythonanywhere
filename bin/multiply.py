#!/usr/bin/env python3
#
range_limit = int(input("Enter range limit: "))
multiplier = int(input("Enter multiplier: "))

for iterator in range(1, range_limit + 1):
    print(multiplier, "*", iterator, "=", iterator * multiplier)
