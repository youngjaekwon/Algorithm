from collections import deque

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    t_idx = 0
    b_idx = len(B) - 1
    answer = 0
    
    for a in A:
        if a >= B[t_idx]:
            b_idx -= 1
        else:
            t_idx += 1
            answer += 1
            
    return answer