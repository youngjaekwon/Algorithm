def solution(a, b, n):
    answer = 0
    while n > a - 1:
        x = n // a * b
        answer += x
        n = x + n % a
    return answer