def solution(n, arr1, arr2):
    arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    arr2 = [bin(x)[2:].zfill(n) for x in arr2]
    
    answer = []
    for a, b in zip(arr1, arr2):
        res = ""
        for x, y in zip(list(a), list(b)):
            if x == "1" or y == "1":
                res += "#"
            else:
                res += " "
        answer.append(res)
                
    return answer