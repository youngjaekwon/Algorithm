def solution(places):
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    diali = [[-1, 1], [-1, 1], [-1, -1], [1, 1]]
    dialj = [[-1, -1], [1, 1], [-1, 1], [-1, 1]]
    result = []
    for case in places:
        for i, line in enumerate(case):
            for j, x in enumerate(line):
                if x == "P":
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if (
                            ni < 0
                            or ni > 4
                            or nj < 0
                            or nj > 4
                            or (y := case[ni][nj]) == "X"
                        ):
                            continue
                        if y == "P":
                            result.append(0)
                            break
                        else:
                            nni = ni + di[k]
                            nnj = nj + dj[k]
                            if nni < 0 or nni > 4 or nnj < 0 or nnj > 4:
                                pass
                            elif case[nni][nnj] == "P":
                                result.append(0)
                                break
                            for a in range(2):
                                dni, dnj = i + diali[k][a], j + dialj[k][a]
                                if (
                                    dni < 0
                                    or dni > 4
                                    or dnj < 0
                                    or dnj > 4
                                    or case[dni][dnj] != "P"
                                ):
                                    continue
                                result.append(0)
                                break
                            else:
                                continue
                            break
                    else:
                        continue
                    break
            else:
                continue
            break
        else:
            result.append(1)

    return result