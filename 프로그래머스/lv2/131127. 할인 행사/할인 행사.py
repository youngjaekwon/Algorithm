from collections import Counter

def solution(want, number, discount):
    answer = 0
    num = sum(number)

    target = {}

    for i, k in enumerate(want):
        target[k] = number[i]

    for i, x in enumerate(discount[:len(discount) - num + 1]):
        if dict(Counter(discount[i:i+10])) == target:
            answer += 1
    return answer