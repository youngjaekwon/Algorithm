while True:
    li = list(map(int, input().split()))
    x, y, z = li
    sum_li = sum(li)
    if sum_li == 0:
        break
    if sum_li - max(li) <= max(li):
        print("Invalid")
        continue

    if x == y == z:
        print("Equilateral")
    elif x == y or x == z or y == z:
        print("Isosceles")
    else:
        print("Scalene")