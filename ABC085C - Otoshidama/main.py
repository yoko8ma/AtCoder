n, t = map(int, input().split())
comb = []

if 10000 * n < t:
    print(-1, -1, -1)
    exit(0)

if 1000 * n > t:
    print(-1, -1, -1)
    exit(0)

for i in range(n+1):
    for j in range(n - i + 1):
        k = n - i - j
        m = 10000 * i + 5000 * j + 1000 * k

        if t == m:
            print(i, j, k)
            exit(0)

print(-1, -1, -1)
