def solution(n):
    nums = [1, 1, 2, 4]
    remainders = []
    while n > 0:
        remainder = n % 3
        n //= 3
        if remainder == 0:
            remainders.append(3)
            n -= 1
        else:
            remainders.append(remainder)
            
    remainders = list(reversed(remainders))
    answer = "".join([str(nums[i]) for i in remainders])
        
    return answer