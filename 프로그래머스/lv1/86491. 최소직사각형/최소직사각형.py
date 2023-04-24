def solution(sizes):
    sizes = list(map(sorted, sizes))
    width = [l[0] for l in sizes]
    length = [l[1] for l in sizes]

    return sorted(width, reverse=True)[0] * sorted(length, reverse=True)[0]