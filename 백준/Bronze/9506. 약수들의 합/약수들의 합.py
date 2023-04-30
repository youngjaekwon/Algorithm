while True:
    N = int(input())

    if N == -1:
        break

    l = []

    for i in range(1, N):
        if N % i == 0:
            l.append(i)

    if sum(l) == N:
        print(f"{N} = {' + '.join(map(str, l))}")
    else:
        print(f"{N} is NOT perfect.")