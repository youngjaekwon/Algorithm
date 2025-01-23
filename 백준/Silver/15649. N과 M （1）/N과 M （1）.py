N, M = list(map(int, input().split()))


arr = list(range(1, N + 1))


answers = []


def sol(li, il):
    if len(il) == M:
        answers.append(il)
        return

    for v in li:
        tmp = list(li)
        tmp.remove(v)
        sol(tmp, il + [v])


for v in arr:
    tmp = list(arr)
    tmp.remove(v)
    sol(tmp, [v])


for answer in answers:
    print(" ".join([str(n) for n in answer]))