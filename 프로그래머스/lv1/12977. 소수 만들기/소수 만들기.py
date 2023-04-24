def get_primes(max_value):
    is_prime = [True] * (max_value + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_value ** (1/2)) + 1):
        if is_prime[i]:
            for j in range(i ** 2, max_value + 1, i):
                is_prime[j] = False
    return [i for i, v in enumerate(is_prime) if v]

def solution(nums):
    max_value = sum(sorted(nums, reverse=True)[0:3])
    primes = get_primes(max_value)
    answer = 0
    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i + 1:]):
            for z in primes:
                if z - x - y in nums[i + 1:][j + 1:]:
                    answer += 1
    return answer