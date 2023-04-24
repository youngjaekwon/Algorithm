def solution(arr):
    mx = max(arr)
    x = 1
    while True:
        result = True
        num = mx * x
        for i in arr:
            if num % i != 0:
                result = False
                break
        if result:
            break
        else:
            x += 1

    return num