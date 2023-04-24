def solution(brown, yellow):
    total = brown + yellow
    li = list()
    
    for i in range(1, round(total ** (1/2)) + 1):
        if not total % i:
            li.append(i)
    
    for i in li:
        width = int(total / i)
        length = i

        if (width + length) * 2 - 4 == brown:
            return [width, length]