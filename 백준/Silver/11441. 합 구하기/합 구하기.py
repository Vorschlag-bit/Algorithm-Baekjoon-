from sys import stdin as input

n = int(input.readline())

arr = [0] + list(map(int,input.readline().split()))

result = []

m = int(input.readline())

for i in range(1,n+1):
    arr[i] += arr[i-1]

for _ in range(m):
    i,j = map(int,input.readline().split())
    result.append(str(arr[j] - arr[i-1]))

print('\n'.join(result))