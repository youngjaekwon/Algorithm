def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for_del = []
        f = False
        p = False
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                if i == 0:
                    f = True
                    p = True
                    for_del.append(i)
                if i != 0 and f and p:
                    for_del.append(i)
                    p = True
            else:
                p = False
                    
        if for_del:
            progresses = [v for i, v in enumerate(progresses) if i not in for_del]
            speeds = [v for i, v in enumerate(speeds) if i not in for_del]
            answer.append(len(for_del))
        f = False
    
    return answer