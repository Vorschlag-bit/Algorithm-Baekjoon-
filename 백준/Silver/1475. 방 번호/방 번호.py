num = input()

#  6이랑 9가 다른 숫자랑 섞여 있는 경우, 두 숫자 제외 최소 개수가 정답
# 6과 9로만 이뤄진 경우, (6 + 9) / 2 가 정답
n = [0] * 10
for i in range(len(num)):
    idx = int(num[i])
    n[idx] += 1
ans1 = 0 
for i in range(10):
    if i != 6 and i != 9:
        ans1 = max(ans1, n[i])
ans2 = (n[6] + n[9] + 1) // 2
print(max(ans1, ans2))