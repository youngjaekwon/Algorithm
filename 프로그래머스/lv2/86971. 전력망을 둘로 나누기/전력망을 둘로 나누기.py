def get_nodes(wires, start):
    stack = [start]
    visited = set()
    while stack:
        start = stack.pop()
        if start in visited:
            continue
        visited.add(start)
        for x, y in wires:
            if x == start:
                stack.append(y)
            elif y == start:
                stack.append(x)
    return len(visited)


def solution(n, wires):
    answer = float("inf")
    for i, v in enumerate(wires):
        x, y = v
        w = list(wires)
        w.pop(i)
        s1 = get_nodes(w, x)
        s2 = get_nodes(w, y)
        if (d := abs(s1 - s2)) < answer:
            answer = d
    return answer