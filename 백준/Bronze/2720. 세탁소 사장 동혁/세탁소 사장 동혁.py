T = int(input())
CASES = [int(input()) for _ in range(T)]
d = {0: 25, 1: 10, 2: 5, 3: 1}

for case in CASES:
    answer = [""] * 4
    for i, v in d.items():
        x, case = case // v, case % v
        answer[i] = str(x)
    print(" ".join(answer))