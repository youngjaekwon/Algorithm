from functools import reduce

T = int(input())
M = [list(map(int, input().split())) for _ in range(T)]

for A, B in M:
    l = []
    while True:
        for i in range(2, max(A, B) + 1):
            if A % i == 0 and B % i == 0:
                l.append(i)
                A //= i
                B //= i
                break
        else:
            l.append(A)
            l.append(B)
            break

    print(reduce(lambda x, y: x * y, l))