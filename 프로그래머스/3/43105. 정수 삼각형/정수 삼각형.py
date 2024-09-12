def solution(triangle):
    cp = [triangle[0]]

    for i, row in enumerate(triangle[1:]):
        tmp = []
        for j, v in enumerate(row):

            if j == len(row) - 1:
                vp = cp[i][j - 1]
            elif j > 0:
                vp = max(cp[i][j - 1], cp[i][j])
            else:
                vp = cp[i][j]
            tmp.append(v + vp)
        cp.append(tmp)

    return max(cp[-1])