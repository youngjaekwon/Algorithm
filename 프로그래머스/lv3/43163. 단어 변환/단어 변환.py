from collections import deque


def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = [False for _ in words]
    x = len(begin) - 1

    while queue:
        v, distance = queue.popleft()

        if v == target:
            return distance

        for i, word in enumerate(words):
            cnt = 0
            for j, c in enumerate(word):
                if c == v[j]:
                    cnt += 1
            if cnt == x and not visited[i]:
                visited[i] = True
                queue.append((word, distance + 1))

    return 0