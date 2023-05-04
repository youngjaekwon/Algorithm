K, N, M = list(map(int, input().split()))
print(K * N - M if K * N > M else 0)