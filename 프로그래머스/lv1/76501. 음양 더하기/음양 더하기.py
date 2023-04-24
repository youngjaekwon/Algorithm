def solution(absolutes, signs):
    return sum([v if signs[i] else -v for i, v in enumerate(absolutes)])