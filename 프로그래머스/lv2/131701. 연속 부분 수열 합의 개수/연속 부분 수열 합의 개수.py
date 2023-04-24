def solution(elements):
    mx = len(elements)
    elements_double = elements * 2
    res = set()
    for i in range(1, mx + 1):
        for j in range(0, mx):
            x = sum(elements_double[j : j + i])
            res.add(x)

    return len(res)