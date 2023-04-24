def solution(n, computers):
    visited = set()

    def dfs(v):
        if v not in visited:
            visited.add(v)

            for neighbor, is_connected in enumerate(computers[v]):
                if is_connected and neighbor not in visited:
                    dfs(neighbor)
            else:
                return 1
        else:
            return 0

    return sum([dfs(i) for i in range(n)])