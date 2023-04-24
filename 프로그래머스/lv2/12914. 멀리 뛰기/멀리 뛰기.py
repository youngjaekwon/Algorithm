def f(x):
    res = 1
    for i in range(x):
        res *= i + 1

    return res

def solution(n):
    single = int(n)
    double = 0
    answer = 0
    while single + (double * 2) == n and single >= 0 and double >= 0:
        x = single + double
        y = min(single, double)
        answer += int(f(x) // (f(x - y) * f(y)))
        single -= 2
        double += 1
    return answer % 1234567