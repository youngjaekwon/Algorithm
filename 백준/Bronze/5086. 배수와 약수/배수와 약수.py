while True:
    N, M = list(map(int, input().split()))

    if N == M == 0:
        break

    if N > M and N % M == 0:
        print("multiple")
    elif M > N and M % N == 0:
        print("factor")
    else:
        print("neither")