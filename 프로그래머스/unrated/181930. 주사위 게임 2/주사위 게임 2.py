def solution(a, b, c):
    target = (a, b, c)
    result = (a + b + c)
    if (set_target := len(set(target))) < 3:
        result *= sum(map(lambda x: x ** 2, target))
    if set_target == 1:
        result *= sum(map(lambda x: x ** 3, target))
    return result