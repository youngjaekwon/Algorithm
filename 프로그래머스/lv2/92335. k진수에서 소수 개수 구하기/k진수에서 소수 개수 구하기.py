def get_str(n, k):
    res = ""

    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)

    return res[::-1]

def is_decimal(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    target = get_str(n, k)
    numbers = target.split('0')
    answer = []
    for number in numbers:
        if not number :
            continue
        if is_decimal(int(number)):
            answer.append(number)

    return len(answer)

solution(110011, 10)