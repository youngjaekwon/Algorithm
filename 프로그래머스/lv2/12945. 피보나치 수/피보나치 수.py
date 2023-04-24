def solution(n):
    l = [0, 1]
    
    for i in range(2, n + 1):
        x = l[i - 1] + l[i - 2]
        l.append(x)
        
    return l[-1] % 1234567