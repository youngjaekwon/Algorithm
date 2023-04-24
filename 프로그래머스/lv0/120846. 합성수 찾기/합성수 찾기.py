from collections import Counter
def solution(n):
    return len([k for k, v in Counter([i for i in range(1, n + 1) for j in range(1, i + 1) if i % j == 0]).items() if v > 2])