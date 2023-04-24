def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, number in enumerate(numbers):
        if not stack:
            stack.append((i, number))
        else:
            while stack and stack[-1][1] < number:
                j, number2 = stack.pop()
                answer[j] = number
            stack.append((i, number))
    
    return answer