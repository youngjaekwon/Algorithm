def solution(n):
    answer = 1
    tmp = 1
    while tmp <= n:
        answer += 1
        tmp *= answer
    return answer - 1