def solution(common):
    z, y, x = common[-3:]
    if (
        y != 0 and z != 0 and x / y == y / z
    ):
        return x * (x / y)
    else:
        return x + (x - y)