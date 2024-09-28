import heapq

def solution(n, k, enemy):
    heap = []
    answer = 0
    for e in enemy:
        answer += 1
        if n >= e:
            n -= e
            heapq.heappush(heap, -e)
        elif k:
            if heap:
                t = -(heapq.heappop(heap))
                if t > e:
                    n += t
                    n -= e
                    heapq.heappush(heap, -e)
                else:
                    heapq.heappush(heap, -t)
            k -= 1
        else:
            answer -= 1
            break
    return answer