def solution(n):
    answer = []
    while True:
        for i in range(2, n + 1):
            if not n % i:
                answer.append(i)
                n //= i
                break
        else:
             break
    return sorted(set(answer))