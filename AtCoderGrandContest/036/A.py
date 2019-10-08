# A - Triangle
import time
import math
from functools import reduce

#試し割法
def trial_division(n):
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    #リストが空ならそれは素数
    if not factor:
        return -1
    else:
        factor.append(n)
        return factor

s = int(input())
l = 10 ** 9

if s < l:
    print(0, 0, 0, 1, s, 0)
    exit()

f = trial_division(s)
f.sort()
print(f)

if f == -1:
    print(0, 0, 0, 1, s, 0)
    exit()

print(l)
m = f.pop(0)

while True:
    n = f.pop(0)
    print(m * n, l)
    print(m * n > l)
    if m * n > l:
        print(0, 0, 0, m, reduce(lambda x, y: x * y, f) * n, 0)
        exit()
    m *= n
