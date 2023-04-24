def solution(dirs):
    cur = (0, 0)
    res = []

    for k in dirs:
        if k == "U":
            if (y:=cur[1] + 1) <= 5:
                x = cur[0]
                cur = (x, y)
                res.append(("y", x, (min(y-1,y), max(y-1,y))))
        elif k == "D":
            if (y:=cur[1] - 1) >= -5:
                x = cur[0]
                cur = (x, y)
                res.append(("y", x, (min(y+1,y), max(y+1,y))))
        elif k == "R":
            if (x:=cur[0] + 1) <= 5:
                y = cur[1]
                cur = (x, y)
                res.append(("x", y, (min(x-1,x), max(x-1,x))))
        elif k == "L":
            if (x:=cur[0] - 1) >= -5:
                y = cur[1]
                cur = (x, y)
                res.append(("x", y, (min(x+1,x), max(x+1,x))))
    return len(set(res))