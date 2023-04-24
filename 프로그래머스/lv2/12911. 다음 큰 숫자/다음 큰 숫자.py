def solution(n):
    x = bin(n)[2:].count("1")
    a = n + 1
    while bin(a)[2:].count("1") != x:
        a += 1
    return a