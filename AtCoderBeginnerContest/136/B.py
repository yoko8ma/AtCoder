import math

n = int(input())

l = math.log10(n)

cnt = 0

if l < 1:
    print(n)
elif l < 2:
    print(9)
elif l < 3:
    print(9 + n - 99)
elif l < 4:
    print(9 + 999 - 99)
elif l < 5:
    print(9 + 999 - 99 + n - 9999)
else:
    print(9 +999 - 99 + 99999 - 9999)
