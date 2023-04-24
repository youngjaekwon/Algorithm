def solution(babbling):
    target = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        tmp = []
        for x in target:
            if x in word:
                tmp.append((word.find(x), x))
        res = "".join([x[1] for x in sorted(tmp, key=lambda y: y[0])])
        if word == res:
            answer += 1
    return answer