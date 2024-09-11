from collections import deque

def solution(maps):
    points = []
    for i, row in enumerate(maps):
        for j, v in enumerate(row):
            if v.isnumeric():
                points.append((i, j))
    if not points:
        return [-1]
    
    n, m = len(maps), len(maps[0])
    answers = []
    visited = set()
    for x, y in points:
        if (x, y) in visited:
            continue
        stack = deque([(x, y)])
        visited.add((x, y))
        answer = 0
        while stack:
            x, y = stack.pop()
            answer += int(maps[x][y])
            
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                xp, yp = x + dx, y + dy
                if 0 <= xp < n and 0 <= yp < m and (xp, yp) not in visited and maps[xp][yp] != "X":
                    stack.append((xp, yp))
                    visited.add((xp, yp))
        answers.append(answer)
    answers.sort()
    return answers