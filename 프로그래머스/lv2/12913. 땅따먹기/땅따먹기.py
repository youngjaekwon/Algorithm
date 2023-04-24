def solution(land):
    mem = [[0 for _ in land[0]] for _ in land]
    mem[0] = list(land[0])

    for i, f in enumerate(land):
        if i == 0:
            continue
        for j, v in enumerate(f):
            max_value = max([v for i, v in enumerate(mem[i-1]) if i != j])
            mem[i][j] = max_value + v
    
    return max(mem[-1])