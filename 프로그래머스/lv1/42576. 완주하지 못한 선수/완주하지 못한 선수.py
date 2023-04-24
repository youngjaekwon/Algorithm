from collections import Counter

def solution(participant, completion):
    return [k for k, v in Counter(participant + completion).items() if v % 2 != 0][0]