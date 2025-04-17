def solution(m, n, board):
    answer = 0
    arr = [[''] * n for _ in range(m)]
    for i,b in enumerate(board):
        for j,char in enumerate(b):
            arr[i][j] = char
    while True:
        delete = set()
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] != 0 and arr[i][j] == arr[i+1][j] and arr[i+1][j] == arr[i][j+1] and arr[i][j+1] == arr[i+1][j+1]:
                    delete |= {(i,j), (i+1,j), (i,j+1), (i+1,j+1)}

        if not delete: break
        answer += len(delete)
        for x,y in delete:
            arr[x][y] = 0
        
        # 중력 발동
        for i in range(m-1):
            for j in range(n):
                p = i
                while 0 <= p and arr[p][j] != 0 and arr[p+1][j] == 0:
                    arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
                    p -= 1
    return answer