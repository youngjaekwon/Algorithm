def solution(quiz):
    answer = []
    for x in quiz:
        l = x.split(" = ")
        answer.append("O" if eval(l[0]) == int(l[1]) else "X")
    return answer