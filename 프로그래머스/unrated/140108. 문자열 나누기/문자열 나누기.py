from collections import deque

def solution(s):
    if not s:
        return 0
    s = deque(s)
    x = s[0]
    cnt_x = 0
    cnt_others = 0
    answer = 0

    while s:
        y = s.popleft()
        if y == x:
            cnt_x += 1
        else:
            cnt_others += 1

        if cnt_x == cnt_others:
            answer += 1
            x = s[0] if s else -1
            cnt_x = 0
            cnt_others = 0

    return answer + 1 if cnt_x or cnt_others else answer