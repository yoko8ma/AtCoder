# B - 0 or 1 Swap
n = int(input())
p = list(map(int, input().split()))

lt_count = 0
gt_count = 0

for i in range(n):
    print(i)
    if i < n-1 and p[i] > p[i+1]:
        gt_count += 1
    elif i >= 2 and p[i] < p[i-1]:
        lt_count += 1

    print(lt_count, gt_count)
if lt_count == 1 and gt_count == 1:
    print('YES')
elif lt_count == 0 and gt_count == 0:
    print('YES')
else:
    print('NO')
