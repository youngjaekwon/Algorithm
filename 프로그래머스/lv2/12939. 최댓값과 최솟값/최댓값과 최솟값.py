def solution(s):
    l = list(map(str, sorted(map(int, s.split(" ")))))
    return " ".join([l[0], l[-1]])