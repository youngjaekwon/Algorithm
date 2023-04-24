def solution(k, m, score):
    score.sort()
    answer = 0
    for i in range(k, 0, -1):
        idx = score.index(i) if i in score else -1
        if idx != -1:
            score, tmp = score[:idx], score[idx:]
            tmp = len(tmp)
            answer += i * m * (tmp // m)
            score.extend([i] * (tmp % m))
            
    return answer