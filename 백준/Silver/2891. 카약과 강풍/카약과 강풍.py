N, S, R = list(map(int, input().split()))
D = sorted(list(map(int, input().split())))
M = sorted(list(map(int, input().split())))
l = list()
for i, I in enumerate(range(1, N + 1)):
    if I in D and I in M:
        D.remove(I)
        M.remove(I)
        l.append(1)
    elif I in D:
        l.append(0)
    else:
        l.append(1)

for i in M:
    if i - 1 in D:
        l[i - 2] = 1
        D.remove(i - 1)
    elif i + 1 in D:
        l[i] = 1
        D.remove(i + 1)

print(l.count(0))