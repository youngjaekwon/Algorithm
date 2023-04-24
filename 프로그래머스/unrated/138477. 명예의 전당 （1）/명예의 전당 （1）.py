def solution(k, score):
    answer = []
    rank = []
    for s in score:
        if len(rank) < k:
            rank.append(s)
        elif s > min(rank):
            rank.remove(min(rank))
            rank.append(s)
        answer.append(min(rank))
    return answer