from sys import stdin as input

while True:
    a, b, c = map(int, input.readline().split())
    if a == b == c == 0:
        break
    l = sorted([a, b, c])

    if l[2] >= l[0] + l[1]:
        print("Invalid")
        continue

    if l[0] == l[2]:
        print("Equilateral")
    elif l[0] == l[1] or l[1] == l[2]:
        print("Isosceles")
    else:
        print("Scalene")