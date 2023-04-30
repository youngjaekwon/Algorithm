from math import ceil

A, B, V = list(map(int, input().split()))

print(ceil((V - A) / (A - B)) + 1)