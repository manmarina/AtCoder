N = int(input())

ans = 0
for i in range(3, 15 + 1, 3):  # コンマの位置3桁目から15桁目まで3桁区切りで考える
    if N // 10**i > 0:  # Nがi桁以上の場合
        ans += N - 10**i + 1  # i桁以上の数の合計（その桁のコンマが付加される数）を加算する
print(ans)

"""
場合分け系
解説よりもシンプルなコードが書けた！
https://atcoder.jp/contests/abc195/editorial/837

https://atcoder.jp/contests/abc195/tasks/abc195_c
"""
