from collections import deque
from heapq import heappush, heappop


class State:
    def __init__(self, cost, minerals, picks):
        self.minerals = minerals
        self.cost = cost
        self.picks = picks

    def __lt__(self, other):
        return self.cost < other.cost

    def datas(self):
        return self.cost, self.minerals, self.picks


def solution(picks, minerals):
    d = {
        0: {"diamond": 1, "iron": 1, "stone": 1},
        1: {"diamond": 5, "iron": 1, "stone": 1},
        2: {"diamond": 25, "iron": 5, "stone": 1},
    }
    minerals = deque(minerals)
    heap = []
    heappush(heap, State(0, minerals, picks))

    while heap:
        status = heappop(heap)
        cost, minerals, picks = status.datas()
        if sum(status.picks) == 0 or not minerals:
            if heap:
                heappush(heap, status)
            else:
                return status.cost
        new_minerals = deque(minerals)
        next_five = [new_minerals.popleft() for _ in range(5) if new_minerals]
        picks_cnt = 0
        for i, v in enumerate(picks):
            if v:
                picks_cnt += 1
                c = sum([d[i][mineral] for mineral in next_five])
                picks_copy = list(picks)
                picks_copy[i] -= 1
                heappush(heap, State(cost + c, new_minerals, picks_copy))
        if not picks_cnt or not minerals:
            break

    cost, minerals, picks = heappop(heap).datas()

    return cost