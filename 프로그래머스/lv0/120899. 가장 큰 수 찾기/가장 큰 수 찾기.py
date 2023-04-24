def solution(array):
    max_num = 0
    max_index = 0
    for i, v in enumerate(array):
        if v > max_num:
            max_num = v
            max_index = i
    return [max_num, max_index]