from collections import deque

def solution(priorities, location):
    answer = 0
    lnum = priorities[location]
    priorities[location] = -1
    p = deque(priorities)

    while location > -1:
        x = p.popleft()
        for y in p:
            if x == -1:
                if lnum < y:
                    p.append(x)
                    break
            elif x < y or x < lnum:
                p.append(x)
                break
        else:
            answer += 1

        if -1 not in p:
            location = -1

    return answer