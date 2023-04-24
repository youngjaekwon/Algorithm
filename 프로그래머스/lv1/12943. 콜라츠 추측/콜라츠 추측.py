def solution(num):
    if num == 1:
        return 0
    cnt = 0
    l = list()
    while cnt <= 500:
        if not num % 2:
            num = num / 2
            l.append(num)
        else:
            num = num * 3 + 1
            l.append(num)
        
        if num == 1:
            return len(l)
        else:
            cnt += 1
        
    return -1
    