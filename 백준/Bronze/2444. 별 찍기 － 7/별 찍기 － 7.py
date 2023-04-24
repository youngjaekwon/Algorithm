N = int(input())
s = N * 2 - 1

for i in list(range(1, N + 1)) + list(range(N - 1, 0, -1)):
    stars = (i - 1) * 2 + 1
    spaces = (s - stars) // 2
    print(f"{' ' * spaces}{'*' * stars}")