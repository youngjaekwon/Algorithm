def solution(s):
    return " ".join([x[0].upper() + x[1:].lower() if len(x) > 1 else x.upper() for x in s.split(" ") ])