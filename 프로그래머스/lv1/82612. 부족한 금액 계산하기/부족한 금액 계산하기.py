def solution(price, money, count):
    total = sum([i * price for i in range(1, count + 1)])
    return abs(money - total) if total > money else 0