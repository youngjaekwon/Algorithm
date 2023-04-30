N = int(input())
M = int(input())

l = list()

for i in range(N, M + 1):
    if i != 1 and len([x for x in range(2, i) if i % x == 0]) == 0:
        l.append(i)

if not l:
    print(-1)
else:
    print(sum(l))
    print(min(l))