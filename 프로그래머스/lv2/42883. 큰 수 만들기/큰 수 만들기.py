def solution(number, k):
    stack = []
    for num in number:
        while k and stack and int(stack[-1]) < int(num):
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k:
        stack = stack[:-k]

    return "".join(stack)