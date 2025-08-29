from collections import defaultdict

N = int(input())
ST = [tuple(input().split()) for _ in range(N)]

# print(ST)

owners = defaultdict(set)           # name -> {indices who have this name}
for i, (s, t) in enumerate(ST):
    owners[s].add(i)
    owners[t].add(i)                # s==t でも set なので同一人物は1人として数えられる

# print(owners)

for i, (s, t) in enumerate(ST):
    s_conflict = any(j != i for j in owners[s])  # 自分以外に使える人がいる？
    t_conflict = any(j != i for j in owners[t])
    if s_conflict and t_conflict:  # 名字も名前も衝突するときはNo
        print("No")
        break
else:
    print("Yes")
