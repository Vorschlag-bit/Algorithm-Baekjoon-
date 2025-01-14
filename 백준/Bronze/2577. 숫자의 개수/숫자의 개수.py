idx = [0] * 10

num = 1
for i in range(3):
    n = int(input())
    num *= n
num = str(num)
for i in range(len(num)):
    n = int(num[i])
    idx[n] += 1

for i in range(10):
    print(idx[i])