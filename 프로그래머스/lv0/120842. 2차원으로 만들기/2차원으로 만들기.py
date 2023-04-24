def solution(num_list, n):
    answer = []
    tmp = []
    for num in num_list:
        tmp.append(num)
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
    return answer