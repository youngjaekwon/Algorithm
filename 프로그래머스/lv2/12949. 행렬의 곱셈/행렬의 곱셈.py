def solution(arr1, arr2):
    answer = []
    for row in arr1:
        li = []
        for i in range(len(arr2[0])):
            res = 0
            for j, x in enumerate(row):
                res += x * arr2[j][i]
            li.append(res)
        answer.append(li)

    return answer