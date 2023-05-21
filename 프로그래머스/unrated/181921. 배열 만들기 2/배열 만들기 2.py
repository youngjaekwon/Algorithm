from itertools import product

def solution(l, r):
    answer = []
    targets = [0, 5]
    for i in range(len(str(l)), len(str(r)) + 1):
        for v in product(targets, repeat=i):
            num = int("".join(map(str, v)))
            if l <= num <= r and num not in answer:
                answer.append(num)
    return answer if answer else [-1]