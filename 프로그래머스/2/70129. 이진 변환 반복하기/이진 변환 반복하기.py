def solution(s):
    c, z = 0, 0
    while s != "1":
        l1 = len(s)
        s = s.replace("0", "")
        l2 = len(s)
        z += l1 - l2
        c += 1
        s = f"{l2:b}"
    return [c, z]