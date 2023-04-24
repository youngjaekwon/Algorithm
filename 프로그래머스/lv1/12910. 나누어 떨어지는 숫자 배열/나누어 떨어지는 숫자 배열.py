def solution(arr, divisor):
    l = [i for i in arr if not i % divisor]
    return sorted(l) if l else [-1]