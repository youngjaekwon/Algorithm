def check(a, b):
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0:
            return i
    return -1

def solution(a, b):
    while (i := check(a, b)) != -1:
        a //= i
        b //= i
    d = 2
    l = set()
    while d <= b:
        if b % d == 0:
            l.add(d)
            b //= d
        else:
            d += 1
    return 1 if not (l - {2, 5}) else 2