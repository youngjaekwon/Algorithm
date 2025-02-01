T = int(input())
arr = [list(input()) for _ in range(T)]

for s in arr:
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")
