def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = list(reversed(deliveries))
    pickups = list(reversed(pickups))

    dt, pt = 0, 0
    i = 0
    while i < n:
        d, p = deliveries[i], pickups[i]
        if (d != 0 or p != 0) and dt == pt == 0:
            answer += (n - i) * 2
        if dt + d > cap or pt + p > cap:
            deliveries[i] = d - (cap - dt)
            pickups[i] = p - (cap - pt)
            dt, pt = 0, 0
        else:
            dt += d
            pt += p
            i += 1
            if dt == cap == pt:
                dt, pt = 0, 0

    return answer