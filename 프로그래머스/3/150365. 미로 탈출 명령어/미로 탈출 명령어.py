import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    xarr = [1, 0, 0, -1]
    yarr = [0, -1, 1, 0]
    commands = "dlru"
    result = ["z" * k]

    def backtrack(x, y, k, path):
        if result[0] <= path:
            return
        if x == r and y == c and k == 0:
            result[0] = path
            return
        if k == 0:
            return
        remain = abs(x - r) + abs(y - c)
        if remain > k:
            return
        if not (remain % 2) and k % 2:
            return
        
        for i in range(4):
            nx, ny = x + xarr[i], y + yarr[i]
            if 1 <= nx <= n and 1 <= ny <= m:
                backtrack(nx, ny, k-1, path + commands[i])

    backtrack(x, y, k, "")
    return result[0] if "z" not in result[0] else "impossible"