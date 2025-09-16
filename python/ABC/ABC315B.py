M = int(input())
D = list(map(int, input().split()))

# 累積和配列を作成
cs = [D[0]]
for i in range(1, M):
    cs.append(cs[i - 1] + D[i])
# print(cs)

# 一年の真ん中の日を決定
mid = (cs[-1] + 1) // 2
# print(mid)

# 月と日を特定
for i in range(M):
    if mid <= cs[i] and i == 0:
        print(i + 1, mid)
        break
    elif mid <= cs[i]:
        print(i + 1, mid - cs[i - 1])
        break
