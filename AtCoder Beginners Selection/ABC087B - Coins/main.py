a = int(input())    # 500
b = int(input())    # 100
c = int(input())    #  50
x = int(input())    # 合計

cnt = 0
i = 0
for i in range(a+1):
    j = 0
    for j in range(b+1):
        k = 0
        for k in range(c+1):
            t = 500 * i + 100 * j + 50 * k
            if t == x:
                cnt += 1

print(cnt)
