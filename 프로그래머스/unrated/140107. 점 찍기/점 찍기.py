def solution(k, d):
    res = 0

    for i in range(d + 1):
        if i % k == 0:
            y_max = int((d ** 2 - i ** 2) ** 0.5)
            res += int(y_max / k) + 1
        else:
            continue

    return res