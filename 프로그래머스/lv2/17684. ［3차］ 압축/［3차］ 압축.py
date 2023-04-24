from collections import deque

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def solution(msg):
    answer = []
    msg = deque(msg)
    tmp = ""
    while msg:
        nxt = msg.popleft()
        tmp += nxt
        if tmp not in x:
            answer.append(x.index(tmp[:-1]) + 1)
            x.append(tmp)
            msg.appendleft(nxt)
            tmp = ""
    if tmp:
        answer.append(x.index(tmp) + 1)
    return answer