def pack(arr):
    num = arr[0][0]

    for row in arr:
        for v in row:
            if num != v:
                return -1

    return num


def solution(arr):
    answer = [0, 0]
    arrs = [arr]

    while arrs:
        b = arrs.pop(0)
        n = pack(b)
        if n != -1:
            answer[n] += 1
            continue
        lb = len(b)
        hlb = lb // 2
        arrs.append([row[:hlb] for row in b[:hlb]])
        arrs.append([row[:hlb] for row in b[hlb:]])
        arrs.append([row[hlb:] for row in b[:hlb]])
        arrs.append([row[hlb:] for row in b[hlb:]])

    return answer