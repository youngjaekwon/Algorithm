d = dict([(i, chr(55 + i)) for i in range(10, 36)])
N, B = map(int, input().split())
answer = []
while N > 1:
    N, x = N // B, N % B
    if x in d:
        x = d[x]
    answer.append(str(x))
if N:
    answer.append(str(N))
print("".join(answer[::-1]))