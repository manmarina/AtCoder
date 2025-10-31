N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# D[j] = B[C[j] - 1]
D = [B[C[j] - 1] for j in range(N)]
print(D)

# カウント用配列（または辞書でもOK）
cnt = [0] * (N + 1)  # cnt[x] = D[j]=xであるjの個数
for d in D:
    cnt[d] += 1
print(cnt)

ans = 0
for a in A:
    ans += cnt[a]  # Ai = Djとなるjの個数を加算

print(ans)

"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」

hamayanhamayan
https://blog.hamayanhamayan.com/entry/2021/05/22/225302
cnt[x] = D[j]=xであるjの個数を前計算しておく

https://atcoder.jp/contests/abc202/tasks/abc202_c/editorial
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6904b906-72e8-8321-8fa2-7f95fb46f6f9
"""
