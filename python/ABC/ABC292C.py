N = int(input())

# 1. f[k] を前処理：k の約数の個数
f = [0] * (N + 1)  # k -> k の約数の個数
for a in range(1, N + 1):  # 1からNまで
    for k in range(a, N + 1, a):  # aからNまでaの倍数を生成
        f[k] += 1
print(f)


# 2. X = 1..N-1 について、f(X) * f(N-X) を足す
ans = 0
for x in range(1, N):
    ans += f[x] * f[N - x]

print(ans)


"""
工夫して探索の通り数を減らす全探索 + 数学的な気づき系
約数列挙を高速に行い、ある数の約数の個数を求める配列f[k]を作成しておく。

けんちょん
https://drken1215.hatenablog.com/entry/2023/05/16/230900

https://atcoder.jp/contests/abc292/tasks/abc292_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691d7be5-c318-8320-b9b7-332b1e235e2e
"""
