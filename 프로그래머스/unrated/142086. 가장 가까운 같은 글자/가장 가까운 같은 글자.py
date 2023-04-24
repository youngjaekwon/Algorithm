def solution(s):
    answer = []
    for i, c in enumerate(s):
        x = s[:i].rfind(c)
        res = i - x if x != -1 else -1
        answer.append(res)
    return answer