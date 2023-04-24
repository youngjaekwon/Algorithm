from itertools import cycle

types = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
]

def solution(answers):
    answer = []
    for i, type in enumerate(types):
        answer.append((i+1, len([x[0] for x in zip(cycle(type), answers) if x[0] == x[1]])))

    return sorted([x[0] for x in answer if x[1] == max(answer, key=lambda x: x[1])[1]])