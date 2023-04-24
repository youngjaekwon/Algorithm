import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while (x:=heapq.heappop(scoville)) < K:
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, (x + (y * 2)))
        if len(scoville) > 1:
            answer += 1
        elif scoville[0] < K:
            return -1
        else:
            answer += 1
    return answer