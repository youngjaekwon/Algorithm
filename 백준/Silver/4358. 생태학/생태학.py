import sys
from collections import defaultdict

input = sys.stdin.readline

trees = defaultdict(lambda: 0)
total = 0
try:
    while True:
        line = input()
        if line == "":
            break
        line = line.rstrip()
        if line == "":
            continue
        trees[line] += 1
        total += 1
except EOFError:
    pass

for k, v in sorted(trees.items()):
    print(k, f"{round(v / total * 100, 4):.4f}")
