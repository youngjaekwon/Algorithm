def solution(s):
    sign = s[0] if s[0] in ["+", "-"] else None
    s = s[1:] if sign != None else s
    return -int(s) if sign == "-" else int(s)