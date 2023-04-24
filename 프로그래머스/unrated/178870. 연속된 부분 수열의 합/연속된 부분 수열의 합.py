def solution(sequence, k):
    l, r = 0, 0
    ml = len(sequence)
    result = None
    s = 0
    while r < len(sequence) and l < len(sequence):
        s += sequence[r]
        while s > k:
            s -= sequence[l]
            l += 1
        if s == k and r - l < ml:
            result = (l, r)
            ml = r - l
        r += 1

    return result