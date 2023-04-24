from collections import deque

def solution(order):
    sub = deque()
    main = deque(range(1, len(order) + 1))
    order = deque(order)
    res = []
    curr_order = order.popleft()
    curr_main = main.popleft()

    while True:
        if curr_order == -1:
            break
        elif sub and curr_order < sub[-1]:
            break

        if curr_main == curr_order:
            res.append(curr_main)
            curr_main = main.popleft() if main else 0
            curr_order = order.popleft() if order else -1
        elif sub and sub[-1] == curr_order:
            while sub and sub[-1] == curr_order:
                res.append(sub.pop())
                curr_order = order.popleft() if order else -1
        elif main:
            sub.append(curr_main)
            curr_main = main.popleft()

    return len(res)