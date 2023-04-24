def solution(order):
    answer = 0
    order = str(order)
    answer += order.count("3")
    answer += order.count("6")
    answer += order.count("9")
    return answer