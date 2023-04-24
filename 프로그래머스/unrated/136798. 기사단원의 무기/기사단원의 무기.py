def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        measures = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0 and i / j != j:
                measures += 2
            elif i % j == 0:
                measures += 1
        if measures <= limit:
            answer += measures
        else:
            answer += power

    return answer