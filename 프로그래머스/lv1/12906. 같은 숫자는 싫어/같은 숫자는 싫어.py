def solution(arr):
    res = list()
    
    for i in arr:
        if res and res[-1] == i:
            continue
        else:
            res.append(i)
            
    return res