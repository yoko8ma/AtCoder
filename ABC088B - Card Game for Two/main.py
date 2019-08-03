n = int(input())    # カードの枚数
points = list(map(int, input().split()))  # カードのポイント

alice_point = 0
bob_point = 0

while True:
    mi = points.index(max(points))
    alice_point += points.pop(mi)
    if len(points) == 0: break

    mi = points.index(max(points))
    bob_point += points.pop(mi)
    if len(points) == 0: break

print(alice_point - bob_point)
