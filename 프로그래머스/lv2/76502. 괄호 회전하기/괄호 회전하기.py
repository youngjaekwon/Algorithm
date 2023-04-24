ops = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def check(s):
    stack = []
    for c in s:
        if c in [")", "]", "}"]:
            op = ops[c]
            if stack and stack[-1] == op:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    return not stack

def solution(s):
    answer = 0
    for c in s:
        if check(s):
            answer += 1
        s = s[1:] + s[0]
    return answer