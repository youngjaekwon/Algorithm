d = dict([(chr(55 + i), i) for i in range(10, 36)])
N, B = input().split()
B = int(B)
x = 0
answer = 0
for n in list(N)[::-1]:
    if n in d:
        n = d[n]
    answer += int(n) * (B**x)
    x += 1

print(answer)