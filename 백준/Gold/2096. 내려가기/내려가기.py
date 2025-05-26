from sys import stdin as input
n = int(input.readline())
arr = list(map(int,input.readline().split()))
mindp = arr[:]
maxdp = arr[:]
for i in range(1,n):
    a = list(map(int,input.readline().split()))
    maxdp = [max(maxdp[0],maxdp[1])+a[0],max(maxdp)+a[1],max(maxdp[1],maxdp[2])+a[2]]
    mindp = [min(mindp[0],mindp[1])+a[0],min(mindp)+a[1],min(mindp[1],mindp[2])+a[2]]
print(max(maxdp), min(mindp))