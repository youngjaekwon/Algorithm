from functools import cmp_to_key

def compare(x, y):
    if x[0] == y[0]:
        return -1 if x + y < y + x else 1
    return -1 if x < y else 1

def solution(numbers):
    numbers = list(sorted(map(str, numbers), key=cmp_to_key(compare), reverse=True))
    answer = "".join(numbers)
    return answer if answer.replace("0", "") else "0"