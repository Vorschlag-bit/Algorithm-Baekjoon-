import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    dic1 = {}
    dic2 = {}
    str1, str2 = input().split()
    for j in range(len(str1)):
        abc = str1[j]
        dic1[abc] = dic1.get(abc, 0) + 1
    for j in range(len(str2)):
        abc = str2[j]
        dic2[abc] = dic2.get(abc, 0) + 1
    check = True
    for k in dic1.keys():
        if k in dic2.keys() and dic1[k] == dic2[k]:
            continue
        else:
            check = False
            break
    print("Possible" if check else "Impossible")
    