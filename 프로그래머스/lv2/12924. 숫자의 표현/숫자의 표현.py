def solution(n):
    a = round(n / 2)
    answer = 1
    for i in range(1, n):
        total = i
        while total < n:
            i += 1
            total += i
        if total == n:
            answer += 1
    return answer