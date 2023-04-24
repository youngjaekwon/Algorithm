import math

def solution(n,a,b):
    answer = 1
    while True:
        a_next = math.ceil(a / 2)
        b_next = math.ceil(b / 2)

        if a_next == b_next:
            break
        else:
            a = a_next
            b = b_next
            answer += 1

    return answer