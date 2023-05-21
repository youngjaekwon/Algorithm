def solution(num_list):
    e, o = "", ""
    for num in num_list:
        if num % 2:
            e += str(num)
        else:
            o += str(num)
    return eval("+".join([o, e]))