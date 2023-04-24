from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)
    c = c.most_common()

    res, cnt = 0, 0
    for _, v in c:
        res += v
        cnt += 1
        if res >= k:
            break
    return cnt