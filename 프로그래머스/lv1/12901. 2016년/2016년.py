def solution(a, b):
    d = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    l = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return d[(sum(l[:a - 1]) + b - 1) % 7]