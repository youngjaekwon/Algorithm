from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    done = []
    on = deque()
    on_time = deque()
    truck_weights = deque(truck_weights)
    while on or truck_weights:
        on_time = deque([x + 1 for x in on_time])
        for v in on_time:
            if v == bridge_length:
                done.append(on.popleft())
                on_time.popleft()
                break
        if truck_weights:
            x = truck_weights.popleft()
            if sum(on) + x <= weight and len(on) < bridge_length:
                on.append(x)
                on_time.append(0)
            else:
                truck_weights.appendleft(x)
        answer += 1
    return answer