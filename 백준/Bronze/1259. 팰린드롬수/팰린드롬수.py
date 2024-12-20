arr = []

while True:
    n = input()
    if n == '0':
        break
    else:
        arr.append(n)

for n in arr:
    p = True
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            p = False
            break
    print("yes" if p else "no")