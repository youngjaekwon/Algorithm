def fun(denum, num):
    x = -1
    mx = max([denum, num])
    mn = min([denum, num])
    for i in range(2, mn + 1):
        if mx % i == 0 and mn % i == 0:
            x = i
    if x == -1:
        return [denum, num]
    else:
        return fun(denum // x, num // x)

def solution(denum1, num1, denum2, num2):
    mx = max([num1, num2])
    mn = min([num1, num2])
    tmp = mx
    while True:
        if tmp % mn == 0:
            break
        else:
            tmp += mx
    denum1 *= tmp // num1
    num1 = tmp
    denum2 *= tmp // num2
    num2 = tmp
    denum = denum1 + denum2
    num = num1
    res = fun(denum, num)
    return res