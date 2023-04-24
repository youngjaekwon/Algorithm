def solution(n, m, section):
    cnt = 0

    l, r = 0, 0
    while l < len(section) and r < len(section):
        s = section[l]
        e = section[r]

        if e - s + 1 <= m:
            r += 1
        else:
            cnt += 1
            l = r

    if r > l:
        cnt += 1

    return cnt