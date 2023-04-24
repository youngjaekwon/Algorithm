def solution(numbers):
    return sorted({x + y for i, x in enumerate(numbers) for y in numbers[i+1:]})