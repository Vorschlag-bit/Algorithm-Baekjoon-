from sys import stdin as input
n,m = map(int, input.readline().split())
ground = list(map(int, input.readline().split()))
diff = [0] * (n + 2)

for i in range(m):
    a,b,k = map(int, input.readline().split())
    diff[a] += k
    diff[b+1] -=k

for i in range(1,n+1):
    diff[i] += diff[i-1]

for i in range(n):
    ground[i] += diff[i+1]

print(' '.join(map(str, ground)))