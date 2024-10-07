import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            break
        elif not scoville:
            return -1
        answer += 1
        s2 = heapq.heappop(scoville)
        s3 = s1 + (s2 * 2)
        heapq.heappush(scoville, s3)
    return answer