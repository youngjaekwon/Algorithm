def solution(numbers, target):
    def dfs(index, total_sum):
        if index == len(numbers):
            return 1 if total_sum == target else 0
        else:
            return dfs(index + 1, total_sum + numbers[index]) + dfs(
                index + 1, total_sum - numbers[index]
            )

    return dfs(0, 0)