def solution(score):
    scores = [(i, sum(v)/2) for i, v in enumerate(score)]
    scores.sort(reverse=True, key=lambda x: x[1])
    rank = 0
    sames = 1
    curr = 101
    answer = [0] * len(score)
    for x in scores:
        if x[1] < curr:
            rank += sames
            answer[x[0]] = rank
            sames = 1
        else:
            answer[x[0]] = rank
            sames += 1
        curr = x[1]

    return answer