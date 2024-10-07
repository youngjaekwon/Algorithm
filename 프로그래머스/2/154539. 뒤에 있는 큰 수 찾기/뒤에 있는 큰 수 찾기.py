def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i, n in enumerate(numbers):
        while stack and stack[-1][1] < n:
            j, _ = stack.pop()
            answer[j] = n
        stack.append((i, n))
    
    return answer