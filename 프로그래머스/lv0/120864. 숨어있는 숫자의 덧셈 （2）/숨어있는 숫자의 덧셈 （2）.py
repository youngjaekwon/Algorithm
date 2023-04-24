def solution(my_string):
    tmp = ""
    for i, v in enumerate(my_string):
        if v.isalpha():
            tmp += " "
        else:
            tmp += v
    return sum([int(x) for x in tmp.split()])