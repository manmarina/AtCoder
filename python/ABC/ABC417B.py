from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
cnt = Counter(A)  # Aのカウンターを作成

# cntから取り出した数をマイナスする
for b in B:
    if cnt[b] > 0:
        cnt[b] -= 1
# print(cnt)

# cntが正ならcntを減らして正解に追加する
for a in A:
    if cnt[a] > 0:
        cnt[a] -= 1
        ans.append(a)

print(*ans)
