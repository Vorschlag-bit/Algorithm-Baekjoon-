import sys;

n, m = map(int, sys.stdin.readline().strip().split())

board = []
ans = []

for i in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n - 7):
    for j in range(m - 7):
        wi = 0 # 시작점이 흰색일 경우 고쳐야하는 색 개수
        bi = 0 # 시작점이 검은색일 경우 고쳐야하는 색 개수
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if(k + l) % 2 == 0:  # 시작점과 같은 색이여야 하는 칸
                    if board[k][l] == 'B': # 시작점이 검은색일 경우
                        wi += 1 # 짝수번째 블럭이 흰색이라면 wi++
                    else:
                        bi += 1 # 시작점이 흰색인데 짝수번째이 흰색인 경우 bi++
                else: # 시작점과 반대인 색이여야 하는 칸
                    if board[k][l] == 'B': # 검은색일 경우
                        bi += 1 # 검은색 시작의 경우 짝수가 검은색이여야하므로
                    else: # 흰색일 경우
                        wi += 1 # 흰색 시작의 경우 짝수가 흰색이여야하므로
        ans.append(wi)
        ans.append(bi)

print(min(ans))
