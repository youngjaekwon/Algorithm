from math import ceil

A, I = list(map(int, input().split()))

I -= 1
I += 0.01

X = I * A

print(ceil(X))