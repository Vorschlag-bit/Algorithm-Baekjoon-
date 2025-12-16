n = int(input())

# 3 * 2**k = k가 몇 인지 알면, 2**k 27개짜리 피라미드 콘솔에 출력
n //= 3
k = 0
while 2**k < n:
    k += 1
# 가운데가 빈 삼각형 만들기
# 가로
# 5,11,23,47,
c = 5
r = 3
cnt = 0
while cnt < k:
    c = c * 2 + 1
    r *= 2
    cnt += 1
# 세로
# 3,6,12
arr = [[' '] * (c+1) for _ in range(r+1)]
# 0 = 3, 1 = 6, 2 = 12
start = 3 * (2**k)
# 재귀를 통해서 가장 작은 삼각형을 찍을 수 있을 때까지 쪼개기
# 시작점, 레벨
# 1을 예시로 생각해보자. start를 기준으로 왼/오른의 삼각형 시작 꼭짓점을 정확하게 계산할 수 있음
# 2를 예시로 꼭 = 12, 왼 = 6, 오른 = 18
# 1일 경우, start = 6, left = 3, right = 9 -> 3개의 삼각형의 밑변 크기를 기준으로 계산하기
# 2 -> start = 12, left = 6, right = 18
def triangle(r,c,level,x,y):
    global arr
    # level이 0이면 point를 기준으로 가장 작은 삼각형 찍기
    if level == 0:
        # 꼭짓점
        arr[r][c] = '*'
        # 바로 아래 2개
        arr[r+1][c-1],arr[r+1][c+1] = '*', '*'
        # 그 아래 5개
        for i in range(5):
            arr[r+2][c-2+i] = '*'
        return
    
    # 그게 아니면 level - 1한 상태로 꼭/왼/오른 재위
    ex_y = ((y-1) // 2)
    # 12, ex_y = 11 // 2 = 5
    ex_x = x // 2
    # 12 가로, level = 1 기준, 
    # r = 행, c = 열
    triangle(r,c,level-1,ex_x,ex_y)
    triangle(r+ex_x,c-ex_y//2-1,level-1,ex_x,ex_y)
    triangle(r+ex_x,c+ex_y//2+1,level-1,ex_x,ex_y)

triangle(1,start,k,r,c)

for row in arr[1:]:
    print(''.join(row[1:]))