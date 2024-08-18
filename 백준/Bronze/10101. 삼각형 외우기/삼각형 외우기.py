x = [int(input()) for _ in range(3)]
sumx = sum(x)

if sumx != 180:
    print("Error")
else:
    if x[0] == x[1] == x[2]:
        print("Equilateral")
    elif x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
        print("Isosceles")
    else:
        print("Scalene")