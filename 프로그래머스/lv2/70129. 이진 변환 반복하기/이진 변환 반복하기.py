def solution(s):
    zero = 0
    cnt = 0
    
    while s != "1":
        length_origin = len(s)
        s = s.replace("0", "")
        length_removed = len(s)
        zero += length_origin - length_removed
        cnt += 1
        s = bin(length_removed)[2:]
            
    return [cnt, zero]