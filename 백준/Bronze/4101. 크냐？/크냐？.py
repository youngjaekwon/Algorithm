while True:
    A, B = list(map(int, input().split()))
    if A == B == 0:
        break
    result = "Yes" if A > B else "No"
    print(result)