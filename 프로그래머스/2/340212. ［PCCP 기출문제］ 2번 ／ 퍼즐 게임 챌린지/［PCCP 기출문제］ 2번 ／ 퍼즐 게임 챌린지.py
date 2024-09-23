def solution(diffs, times, limit):
    minl, maxl = 1, max(diffs)
    while maxl > minl:
        mid = (maxl + minl) // 2
        count = 0
        prev_t = 0
        for j in range(len(diffs)):
            t = times[j]
            d = diffs[j]
            count += (t + prev_t) * max((d - mid), 0) + t
            prev_t = t
            if count > limit:
                minl = mid + 1
                break
        if count <= limit:
            maxl = mid
    return maxl