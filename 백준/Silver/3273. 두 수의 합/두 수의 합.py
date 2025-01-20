import sys
input = sys.stdin.readline
n = int(input())
seq = input().split()
x = int(input())

max_value = 1000000
arr = [0] * (max_value + 1)

result = 0

for i in range (0, n):
    num = int(seq[i])
    y = x - num
    if 0 <= y <= max_value and arr[y] == 1:
        result += 1
        arr[num] = 1
    else:
        arr[num] = 1
print(result)