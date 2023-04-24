def solution(n, lost, reserve):
    inter = set(lost) & set(reserve)
    lost = [i for i in lost if i not in inter]
    reserve = [i for i in reserve if i not in inter]

    answer = 0
    for i in range(1, n + 1):
        if i not in lost:
            answer += 1
        else:
            if i - 1 in reserve:
                answer += 1
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                answer += 1
                reserve.remove(i + 1)
    return answer