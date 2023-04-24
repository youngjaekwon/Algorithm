def solution(n, m):
    l = sorted([n, m])
    a, b = l[0], l[1]
    x = max([i for i in range(1, a + 1) if not b % i and not a % i])
    y = b
    
    while True:
        if not y % a:
            break
        y += b
    
    return [x, y]