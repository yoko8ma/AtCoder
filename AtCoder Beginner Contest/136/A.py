# A - Transfer
a, b, c = map(int, input().split())
r = c - (a - b)
if r < 0:
    r = 0

print (r)
