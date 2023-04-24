def solution(players, callings):
    rank = dict()
    first = None
    for i, player in enumerate(players):
        f = players[i - 1] if i - 1 >= 0 else None
        if f is None:
            first = player
        r = players[i + 1] if i + 1 < len(players) else None
        rank[player] = (f, r)

    for player in callings:
        pf, pr = rank[player]
        fpf, fpr = rank[pf]
        rank[player] = (fpf, pf)
        rank[pf] = (fpr, pr)
        if fpf is not None:
            rank[fpf] = (rank[fpf][0], player)
        else:
            first = player
        if pr is not None:
            rank[pr] = (pf, rank[pr][1])

    result = [first]
    cur_player = first
    while cur_player is not None:
        cp = rank.pop(cur_player)
        np = cp[1]
        if np is not None:
            result.append(np)
        cur_player = np

    return result