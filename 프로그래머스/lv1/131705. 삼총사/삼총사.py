def solution(number):
    answer = 0
    
    for i, x in enumerate(number):
        for j, y in enumerate(number[i+1:]):
            for k, z in enumerate(number[i+2+j:]):
                if x + y + z == 0:
                    answer += 1
                    
    return answer