N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

l = list()

for A, B, C in M:
    if A == B == C:
        l.append(10000 + A * 1000)
    elif A == B or A == C:
        l.append(1000 + A * 100)
    elif B == C:
        l.append(1000 + B * 100)
    else:
        l.append(max(A, B, C) * 100)

print(max(l))