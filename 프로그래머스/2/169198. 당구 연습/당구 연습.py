"""
상하좌우
상 : x -> 1, y -> 2n - y
하 : x -> 1, y -> -1
좌 : x -> -1, y -> 1
우 : x -> 2m - x, y -> 1
좌상 : x -> -(2m - x), y -> 2n - y
    - (0, n)에 대한 기울기가 같으면서
    - x가 startX보다 작지 않은 경우
우상 : x -> 2m - x, y -> 2n - y
    - (m, n)에 대한 기울기가 같으면서
    - y가 startY보다 크지 않은 경우
좌하 : x -> -1, y -> -1
    - (0, 0)에 대한 기울기가 같으면서
    - x가 startX보다 작지 않은 경우
우하 : x -> -(2m - x), y -> -1
    - (m, 0)에 대한 기울기가 같으면서
    - y가 startY보다 작지 않은 경우
"""

def cal(a, b):
    return abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2

def cal2(a, b):
    return abs(a[1] - b[1]) / abs(a[0] - b[0])

def compare(a, b, c):
    return cal2(a, c) == cal2(b, c)

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