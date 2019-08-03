n, a, b = map(int, input().split())

t = []

for i in range(1, n+1):
    s = sum([int(x) for x in list(str(i))])
    if s >= a and s <= b:
        t.append(i)

print(sum(t))
