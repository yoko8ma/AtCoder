rows = []
n = int(input())
for i in range(n):
    rows.append(list(map(int, input().split())))

position =[0, 0]  # 原点
last_n = 0

for row in rows:
    n = row[0]  # 3
    x_goal = row[1] # 1
    y_goal = row[2] # 2
    goal = [x_goal, y_goal]
    x_diff = x_goal - position[0]
    y_diff = y_goal - position[1]

    if n - last_n < abs(x_diff) + abs(y_diff):
        print('No')
        exit()

    times = n - last_n
    times -= abs(x_diff)
    position[0] = x_goal

    times -= abs(y_diff)
    position[1] = y_goal

    if times % 2 != 0:
        print('No')
        exit()

    last_n = n
print('Yes')
