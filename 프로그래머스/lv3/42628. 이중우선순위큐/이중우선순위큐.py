def solution(operations):
    q = list()
    for operation in operations:
        operation = operation.split(" ")
        num = int(operation[1])

        if (fn := operation[0]) == "I":
            q.append(num)
        elif fn == "D" and q:
            if num > 0:
                q.remove(max(q))
            else:
                q.remove(min(q))

    if q:
        answer = [max(q), min(q)]
    else:
        answer = [0, 0]

    return answer