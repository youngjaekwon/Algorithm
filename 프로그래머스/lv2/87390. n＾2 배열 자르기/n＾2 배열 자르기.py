import math

def solution(n, left, right):
    answer = []
    x = math.ceil((left + 1) / n)
    y = math.ceil((right + 1) / n)

    for i in range(x, y + 1):
        answer.extend([i] * i)
        answer.extend(range(i + 1, n + 1))
    a = left % n
    return answer[a: a + right - left + 1]