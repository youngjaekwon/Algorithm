import sys

input = sys.stdin.readline

N = int(input())
arr = list(set([input().replace("\n", "") for _ in range(N)]))


def compare(a):
    return (len(a), a)


arr.sort(key=compare)

for s in arr:
    print(s)
