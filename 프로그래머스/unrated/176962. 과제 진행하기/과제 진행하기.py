from collections import deque

def solution(plans):
    plans_copy = list()
    for n, t, s in plans:
        tc = list(map(int, t.split(":")))
        plans_copy.append([n, tc[0] * 60 + tc[1], int(s)])
    plans_copy.sort(key=lambda x: x[1])
    now = 0
    done = list()
    queue = deque(plans_copy)
    paused = deque()

    while queue or paused:
        if not queue and paused:
            next_plan = paused.popleft()
        elif paused and now >= queue[0][1]:
            next_plan = queue.popleft()
        elif paused:
            next_plan = paused.popleft()
        else:
            next_plan = queue.popleft()

        name, start, time = next_plan

        x = max(now, start) + time
        if queue and x > (next_now := queue[0][1]):
            next_plan[2] -= next_now - max(now, start)
            now = next_now
            paused.appendleft(next_plan)
        else:
            done.append(name)
            now = x

    return done