N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

queue = []

for i, v in enumerate(M):
    T, P = v
    if i + T <= len(M):
        queue.append((P, M[i + T :]))

max_value = 0

while queue:
    V, M_copy = queue.pop(0)
    if V > max_value:
        max_value = V

    for i, v in enumerate(M_copy):
        T, P = v
        if i + T <= len(M_copy):
            queue.append((V + P, M_copy[i + T :]))

print(max_value)