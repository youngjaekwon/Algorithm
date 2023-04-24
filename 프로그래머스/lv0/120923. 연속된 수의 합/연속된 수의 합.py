def solution(num, total):
    answer = []
    for i in range(-num, total + 1):
        if sum((tmp := range(i, i + num))) == total:
            answer = tmp
            break
    return sorted(answer)