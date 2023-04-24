from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(li):
    res = []
    for i in range(1, len(li)+1):
        res.extend(permutations(li, i))
    return res

def solution(numbers):
    answer = 0
    al = {int("".join(case)) for case in get_permutations(numbers)}
    for i in al:
        if is_prime(i):
            answer += 1
    return answer