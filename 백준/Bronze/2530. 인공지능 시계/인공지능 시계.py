H, M, S = list(map(int, input().split()))

D = int(input())

h, D = D // 3600, D % 3600
m, D = D // 60, D % 60

S += D
if S >= 60:
    S -= 60
    m += 1

M += m
if M >= 60:
    M -= 60
    h += 1

H += h
if H > 23:
    H %= 24

print(H, M, S)