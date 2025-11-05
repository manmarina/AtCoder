N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
# print(LR)

# 城壁の増減を記録
change = [0] * (N + 2)
for l, r in LR:
    change[l] += 1
    change[r + 1] -= 1

# 城壁の累積和を記録
imos = [0] * (N + 1)
for i in range(1, N + 1):
    imos[i] = imos[i - 1] + change[i]

# print(imos)
print(min(imos[1:]))  # 城壁が一番薄いところの厚みを出力

"""
いもす法（Imos法）
（別名：差分配列法、区間加算の高速処理テクニック）
いもす法の典型題！
城壁が一番薄いところの厚みを出力する。

https://atcoder.jp/contests/abc408/tasks/abc408_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690aa8cf-7ae4-8321-96b8-1fbc4e884e51
"""
