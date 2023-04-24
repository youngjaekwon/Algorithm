def solution(food):
    answer = ''
    for i, v in enumerate(food):
        x = str(i)
        answer += x * (v // 2)
    return answer + "0" + "".join(reversed(answer))