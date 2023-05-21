def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        targets = arr[s:e+1]
        if max(targets) <= k:
            answer.append(-1)
        else:
            for v in sorted(targets):
                if v > k:
                    answer.append(v)
                    break
    return answer