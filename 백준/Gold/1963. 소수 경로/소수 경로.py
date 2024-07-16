import math

T = int(input())


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if not x % i:
            return False
    return True


def solution():
    n, np = list(map(int, input().split()))

    count = None
    success = False
    queue = [(0, n)]
    visited = {n}

    while queue:
        c, x = queue.pop(0)
        if x == np:
            success = True
            count = c
            break

        x = str(x)
        for i in range(4):
            y = x[i]
            for j in range(0, 11):
                if i == 0 and j == 0:
                    continue
                elif i == 3 and j in [0, 2, 4, 6, 8]:
                    continue
                j = str(j)
                if j == y:
                    continue
                xp = list(x)
                xp[i] = j
                xp = int("".join(xp))
                if xp not in visited and is_prime_number(xp):
                    queue.append((c + 1, xp))
                    visited.add(xp)

    if success:
        print(count)
    else:
        print("Impossible")


for _ in range(T):
    solution()
