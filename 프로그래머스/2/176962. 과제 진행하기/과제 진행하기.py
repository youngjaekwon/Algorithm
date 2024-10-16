from collections import deque


def cal_time(t, a):
    h, m = list(map(int, t.split(":")))
    a = int(a)
    h += a // 60
    m += a % 60
    if m >= 60:
        h += 1
        m -= 60
    return f"{h}:{m}"


def compare_time(a, b):
    ah, am = list(map(int, a.split(":")))
    bh, bm = list(map(int, b.split(":")))
    a, b = (ah, am), (bh, bm)
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1


def get_diff_time(a, b):
    ah, am = list(map(int, a.split(":")))
    bh, bm = list(map(int, b.split(":")))
    return (ah * 60 + am) - (bh * 60 + bm)


def solution(plans):
    answer = []
    stack = deque()
    plans.sort(key=lambda x: x[1])
    plans = deque(plans)
    current_time = plans[0][1]  # 현재 시간

    def do_plan(plan):
        play_time = int(plan[2])
        if plans:
            diff = get_diff_time(plans[0][1], current_time)
            if diff < play_time:
                play_time -= diff
                plan[2] = str(play_time)
                stack.append(plan)
                return cal_time(current_time, diff)
        answer.append(plan[0])
        return cal_time(current_time, plan[2])

    while plans or stack:
        if not plans:
            s = stack.pop()
            answer.append(s[0])
            continue

        p = plans.popleft()
        res = compare_time(p[1], current_time)

        if res == 1:
            if not stack:
                next_plan = p
                current_time = p[1]
            else:
                next_plan = stack.pop()
                plans.appendleft(p)
        else:
            next_plan = p

        current_time = do_plan(next_plan)

    return answer