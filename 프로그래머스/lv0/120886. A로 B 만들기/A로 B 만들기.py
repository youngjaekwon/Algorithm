def solution(before, after):
    answer = 0
    after = list(after)
    tmp = ""
    for c in before:
        if c in after:
            tmp += c
            after.remove(c)
    return 1 if len(tmp) == len(before) else 0