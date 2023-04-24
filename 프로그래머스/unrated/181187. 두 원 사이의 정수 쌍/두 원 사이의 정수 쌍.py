import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        if r1 >= x:
            y1 = math.ceil(math.sqrt(r1 ** 2 - x ** 2))
        else:
            y1 = 0
        y2 = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        dots = y2 - y1 + 1
        answer += dots

    
    return answer * 4