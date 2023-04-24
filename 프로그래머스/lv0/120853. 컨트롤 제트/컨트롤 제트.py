def solution(s):
    answer = 0
    tmp = -1
    for x in s.split():
        if x == "Z":
            answer -= tmp
        else:
            tmp = int(x)
            answer += tmp
    return answer