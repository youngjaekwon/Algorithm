def solution(prices):
    s = []
    answer = [0 for _ in prices]
    for i, p in enumerate(prices):
        while s and s[-1][-1] > p:
            j, c = s.pop()
            answer[j] = i - j
        s.append((i, p))
    total = len(prices)
    while s:
        i, p = s.pop()
        answer[i] = total - i - 1
    return answer