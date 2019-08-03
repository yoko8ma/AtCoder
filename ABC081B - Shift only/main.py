N = int(input())
A = [] * N
A = list(map(int, input().split()))
c = 0
print(A)
while True:
    if all(item % 2 == 0 for item in A):
        A = [i / 2 for i in A]
        print(A)
        c += 1
    else:
        break

print(c)