def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i, p1 in enumerate(prices):
        while stack:
            j, p2 = stack.pop()
            if p2 > p1:
                answer[j] = i - j
            else:
                stack.append((j, p2))
                break
        stack.append((i, p1))

    for i, p in stack:
        answer[i] = len(prices) - 1 - i
    
    return answer