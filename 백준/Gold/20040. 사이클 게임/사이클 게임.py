from sys import stdin as input

n,m = map(int,input.readline().split())

p = [i for i in range(n)]

def find(num):
    if p[num] == num: return num

    # 경로 압축
    p[num] = find(p[num])
    return p[num]

def union(a,b):
    r_a = find(a)
    r_b = find(b)

    if r_a != r_b:
        if r_a < r_b:
            p[r_b] = r_a
        else :
            p[r_a] = r_b
        return True
    else: return False

for t in range(m):
    a,b = map(int,input.readline().split())
    if find(a) == find(b):
        print(t+1)
        exit()
    union(a,b)
print(0)