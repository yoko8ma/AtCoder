N, Q = map(int, input().split())

s = []

for i in range(N):
    s.append(chr(ord('A') + i))

print(s)
i = 0
while i < N:
    j = 0
    while j < N-1:
        print('? {} {}'.format(s[j], s[j+1]))
        ans = input()

        if(ans == '>'):
            s[j], s[j + 1] = s[j + 1], s[j]
        else:
            break
        print(s)
        j += 1

    i += 1

print('! {}'.format(''.join(s)))
