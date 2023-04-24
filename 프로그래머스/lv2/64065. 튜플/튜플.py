def solution(s):
    s = sorted([c.split(",") for c in s.replace("},{", " ").replace("{", "").replace("}", "").split()], key=lambda x: len(x))
    answer = []
    for c in s:
        answer.extend([int(x) for x in c if int(x) not in answer])
    return answer