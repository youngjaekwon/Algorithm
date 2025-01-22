S = list(input())


def solution():
    stack = []
    value_stack = []

    for c in S:
        if c in ["(", "["]:
            stack.append(c)
            value_stack.append(c)
        else:
            if not stack:
                return 0
            elif c == ")" and stack[-1] == "(":
                if value_stack[-1] == "(":
                    value_stack.pop()
                    value_stack.append(2)
                else:
                    tmp = 0
                    while isinstance(value_stack[-1], int):
                        tmp += value_stack.pop()
                    value_stack.pop()
                    value_stack.append(tmp * 2)

            elif c == "]" and stack[-1] == "[":
                if value_stack[-1] == "[":
                    value_stack.pop()
                    value_stack.append(3)
                else:
                    tmp = 0
                    while isinstance(value_stack[-1], int):
                        tmp += value_stack.pop()
                    value_stack.pop()
                    value_stack.append(tmp * 3)
            else:
                return 0
            stack.pop()

    if stack:
        return 0

    return sum(value_stack)


print(solution())