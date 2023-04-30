N = int(input())
l = list(map(int, input().split()))

cnt = 0

for i in l:
    is_pnum = i != 1 and len([x for x in range(2, i) if i % x == 0]) == 0
    if is_pnum:
        cnt += 1

print(cnt)