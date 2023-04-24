def push(A):
    return A[-1] + A[:-1]

def solution(A, B):
    answer = 0
    for _ in range(len(A)):
        if A == B:
            break
        else:
            A = push(A)
            answer += 1
    else:
        answer = -1
    return answer