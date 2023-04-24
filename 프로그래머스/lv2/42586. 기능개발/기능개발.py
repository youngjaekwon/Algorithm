def solution(progresses, speeds):
    answer = []
    while progresses:
        progresses = list(map(sum, zip(progresses, speeds)))
        cnt = 0
        for x in progresses:
            if x < 100:
                break
            cnt += 1
        progresses = progresses[cnt:]
        speeds = speeds[cnt:]
        if cnt:
            answer.append(cnt)
    return answer