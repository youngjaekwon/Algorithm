p = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    for word in babbling:
        tmp = ""
        lock = ""
        for c in word:
            tmp += c
            if tmp in p and tmp != lock:
                lock = tmp
                tmp = ""
        if not tmp:
            answer += 1
    return answer