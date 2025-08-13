from sys import stdin as input
n = int(input.readline())
switch = list(map(int, input.readline().split()))
m = int(input.readline())
student = []
for _ in range(m):
    gender, num = map(int,input.readline().split())
    student.append((gender,num))
for g,num in student:
    # 0 = base
    base = num - 1
    # 남자인 경우
    if g == 1:
        for idx in range(base,n,num):
            switch[idx] = switch[idx] ^ 1
    # 여자인 경우
    else:
        l = 0
        # base 기준으로 대칭확인
        while base - l >= 0 and base + l < n: 
            if switch[base-l] != switch[base+l]:
                break
            l += 1
        l -= 1
        for i in range(l+1):
            switch[base-i] = switch[base-i] ^ 1
            if i != 0:
                switch[base+i] = switch[base+i] ^ 1 
for i in range(0,n,20):
  print(' '.join(map(str,switch[i:i+20])))