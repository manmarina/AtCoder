from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

need = Counter(B)  # 各値を何個消すか
print(need)

ans = []
for x in A:
    if need[x] > 0:
        need[x] -= 1   # この x は削除
    else:
        ans.append(x)

print(*ans)  # 空なら何も出ない
