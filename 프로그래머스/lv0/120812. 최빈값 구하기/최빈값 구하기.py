from collections import Counter

def solution(array):
    c = Counter(array)
    c = c.most_common()
    return c[0][0] if len(c) == 1 or c[0][1] != c[1][1] else -1