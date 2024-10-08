"""
상하좌우
상 : x -> 1, y -> 2n - y
하 : x -> 1, y -> -1
좌 : x -> -1, y -> 1
우 : x -> 2m - x, y -> 1
"""

def cal(a, b):
    return abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    s = (startX, startY)
    
    for b in balls:
        d = []
        if startX != b[0]:
            d.append(cal(s, (b[0], 2*n - b[1])))
            d.append(cal(s, (b[0], -b[1])))
        elif startY > b[1]:
            d.append(cal(s, (b[0], 2*n - b[1])))
        elif startY < b[1]:
            d.append(cal(s, (b[0], -b[1])))
        if startY != b[1]:
            d.append(cal(s, (-b[0], b[1])))
            d.append(cal(s, (2*m - b[0], b[1])))
        elif startX < b[0]:
            d.append(cal(s, (-b[0], b[1])))
        elif startX > b[0]:
            d.append(cal(s, (2*m - b[0], b[1])))
        answer.append(min(d))
    
    return answer