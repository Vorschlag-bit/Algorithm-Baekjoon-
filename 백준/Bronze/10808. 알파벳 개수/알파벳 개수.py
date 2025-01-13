str = input()

alp = [0] * 26

for i in range(len(str)):
    abc = str[i]
    alp[ord(abc) - 97] += 1
ans = ""
for i in alp:
    ans += f"{i} "

print(ans)