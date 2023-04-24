def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])

    l = -1
    for start, end in targets:
        if l <= start:
            answer += 1
            l = end

    return answer
