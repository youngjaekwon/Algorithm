def solution(n):
    if n == 1: return 1
    li = list()
    while True:
        a, b = n // 3, n % 3
        li.append(b)
        if a < 3:
            li.append(a)
            break
        n = a
    i = "".join(map(str, li))
    return int(i, 3)
    
    