print(sum([x if x > 40 else 40 for x in [int(input()) for _ in range(5)]]) // 5)