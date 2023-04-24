def solution(dots):
    case1 = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    case2 = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])
    case3 = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]) == (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    return 1 if case1 or case2 or case3 else 0