from collections import defaultdict

def solution(survey, choices):
    res = defaultdict(int)
    for i, v in enumerate(choices):
        if v < 4:
            res[survey[i][0]] += 4 - v
        elif v > 4:
            res[survey[i][1]] += v - 4

    answer = ""
    answer += "R" if res.get("R", 0) >= res.get("T", 0) else "T"
    answer += "C" if res.get("C", 0) >= res.get("F", 0) else "F"
    answer += "J" if res.get("J", 0) >= res.get("M", 0) else "M"
    answer += "A" if res.get("A", 0) >= res.get("N", 0) else "N"

    return answer