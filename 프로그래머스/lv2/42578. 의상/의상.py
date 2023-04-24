from collections import defaultdict

def solution(clothes):
    hashed_clothes = defaultdict(list)

    for item in clothes:
        hashed_clothes[item[1]].append(item[0])

    res = [len(li) for li in hashed_clothes.values()]

    answer = 1
    
    for i in res:
        answer *= i + 1

    return int(answer) - 1