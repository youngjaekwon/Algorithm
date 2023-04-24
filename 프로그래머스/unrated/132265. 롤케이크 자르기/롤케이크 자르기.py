from collections import Counter, deque

def solution(topping):
    answer = 0
    all_kind = Counter(topping)
    dq = deque(topping)
    s1 = set()

    while dq:
        x = dq.popleft()
        s1.add(x)
        all_kind[x] -= 1
        if not all_kind[x]:
            del all_kind[x]
        if len(s1) == len(all_kind.keys()):
            answer += 1

    return answer