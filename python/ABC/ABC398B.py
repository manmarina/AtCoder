from itertools import combinations

A = list(map(int, input().split()))

for cards in combinations(A, 5):
    # print(sorted(cards))
    if len(set(cards)) == 2:  # 1枚と4枚でもフルハウスと判定してしまっている
        print("Yes")
        break
else:
    print("No")
