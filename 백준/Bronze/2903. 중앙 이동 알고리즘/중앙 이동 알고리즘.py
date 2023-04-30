N = int(input()) + 1


def f(n):
    if n == 1:
        return 2

    x = f(n - 1)

    return x + x - 1


num = f(N)
print(num**2)