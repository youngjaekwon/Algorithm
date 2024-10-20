from collections import deque

def solution(k, dungeons):
    queue = deque()
    for i, d in enumerate(dungeons):
        queue.append((k - d[1], {i}))
        
    answer = -1    
    while queue:
        k, visited = queue.popleft()
        
        finished = True
        for i, d in enumerate(dungeons):
            if i in visited:
                continue
                
            a, b = d
            if k >= a:
                nv = set(visited)
                nv.add(i)
                queue.append((k - b, nv))
                finished = False
                
        if finished:
            l = len(visited)
            if answer < l:
                answer = l
                
    return answer