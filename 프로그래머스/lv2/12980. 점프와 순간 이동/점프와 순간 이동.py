def solution(n):
    ans = 0
    while n > 1:
        if n % 2 == 1:
            n -= 1
            ans += 1
        n /= 2
    ans += 1
    return ans