def solution(chicken):
    coupon = 0
    answer = 0
    while chicken:
        coupon += chicken % 10
        chicken //= 10
        answer += chicken

    coupon_ = 0
    while coupon:
        coupon_ += coupon % 10
        coupon //= 10
        answer += coupon
    return answer + coupon_ // 10