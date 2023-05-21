def solution(num_list):
    x, y = num_list[-2:]
    return num_list + [y - x] if y > x else num_list + [y * 2] 