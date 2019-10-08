s =  input()
c = [1] * len(s)
t = [0] * len(s)
pos = []

pos.append(c)
print(len(s))
for i in range(20):
    for j in range(len(s)):
        if s[j] == 'R':
            t[j+1] += c[j]
        else:
            t[j-1] += c[j]

    c = t
    t = [0] * len(s)
    print(*c)
