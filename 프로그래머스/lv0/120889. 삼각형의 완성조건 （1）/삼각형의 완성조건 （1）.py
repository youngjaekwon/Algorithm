def solution(sides):
    max_val = max(sides)
    sides.remove(max_val)
    return 1 if max_val < sum(sides) else 2