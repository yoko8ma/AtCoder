import itertools

s = input()
seeds = ['dream', 'dreamer', 'erase', 'eraser']

if len(set(list(''.join(seeds))) | set(list(s))) > 6:
    print('NO')
    exit()

words = seeds

while True:
    if s in words:
        print('YES')
        exit()

    heads = []

    for w in words:
        if s.startswith(w):
            heads.append(w)

    if len(heads) == 0:
        print('NO')
        exit()

    words = list(map("".join, itertools.product(heads, seeds)))

    if min([len(w) for w in words]) > len(s):
        print('NO')
        exit()
