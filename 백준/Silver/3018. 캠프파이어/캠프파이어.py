import sys
n = int(sys.stdin.readline().strip())

e = int(sys.stdin.readline().strip())

# 딕셔너리 초기화
songs = {i: 0 for i in range(1, n+1)}
total = []
for i in range(e):
    # i일차의 노래 = value, j번 사람 = key
    k, *people = map(int, sys.stdin.readline().strip().split())
    people = set(people)
    if 1 in people:
        total.append(people)
    else:
        for song in total:
            # total list 속 set 하나 하나 = song
            for person in people:
                # 오늘 축제에 참석한 사람들과 song의 교집합 찾기
                if person in song: # 1명이라도 있다면, 새로 업데이트 후, 다음 곡으로
                    song.update(people)
                    break

# 모든 사람이 있는 집합으로 시작
ans = set(i for i in range(1, n + 1))
for song in total:
    # 모든 노래를 순회하며 노래와 사람 번호의 교집합 생성
    ans = ans & song
ans = sorted(list(ans))

for a in ans:
    print(a)
