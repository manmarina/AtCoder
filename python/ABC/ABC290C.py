N, K = map(int, input().split())
A = set(map(int, input().split()))  # 重複を削除

A = sorted(A)  # ソート
# print(A)

# 重複を削除したことにより要素数がK未満になっていることがあるので注意！！
for i in range(min(K, len(A))):  # KのみだとREになることがある
    if A[i] != i:
        print(i)
        exit()
else:
    print(i + 1)

"""
問題文の理解が難解系

但し、数列 X に対して MEX(X) は以下の条件を満たす唯一の非負整数 m として定義されます。
    0≤i<m を満たす全ての整数 i が X に含まれる。
    m が X に含まれない。
    -> 「その集合の中に含まれていない最小の非負整数（0以上の整数）」を求める問題

https://atcoder.jp/contests/abc290/tasks/abc290_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
