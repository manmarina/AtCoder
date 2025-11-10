N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# D[j] = B[C[j] - 1]
D = [B[C[j] - 1] for j in range(N)]
print(D)

# カウント用配列（または辞書でもOK）
cnt = [0] * (N + 1)  # D[j] -> D[j]の個数
for d in D:
    cnt[d] += 1
print(cnt)

ans = 0
for a in A:  # すべてのAiを見る
    ans += cnt[a]  # Ai = Djとなるjの個数を加算

print(ans)

"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」

hamayanhamayan
https://blog.hamayanhamayan.com/entry/2021/05/22/225302
B[C[j]]の部分であるが、別途配列Dを考えて、単純にD[j] = B[C[j]]として置き換えると、特に配列の配列として考える必要はなくなる。

これでi,jを全探索しようとすると10^10通りくらいになるので間に合わない。
（全探索はできて10^7くらいまで）
これをiだけ全探索してjは高速に求められる状態にしておくことで解決する。
とあるiを考えると対応するjはA[i]=D[j]であるjである。
よってA[i]=D[j]であるjの個数が前計算されていれば、高速に答えることができることになる。

cnt[x] = D[j]=xであるjの個数

この配列を前計算して作っておこう。
すると、とあるiのとき、条件を満たすjの個数はcnt[A[i]]となる。
これでACが取れる。

https://atcoder.jp/contests/abc202/tasks/abc202_c/editorial
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6904b906-72e8-8321-8fa2-7f95fb46f6f9
"""
