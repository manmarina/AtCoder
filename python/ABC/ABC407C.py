S = input()

Sr = S[::-1]  # 数列を逆にして頭から見てゆく（下1桁からみてゆく）
pre = 0  # 一つ前の桁の数値
ans = 0

# ボタンBを押した回数を加算
for i in range(len(Sr)):
    cur = int(Sr[i])  # 注目する桁
    if cur >= pre:  # 注目する桁の数値が、一つ前の桁の数値より大きい時
        ans += cur - pre  # 差が押した回数となる（同じ値なら押さない！）
        pre = cur  # 一つ前の桁の数値を更新
    else:  # 注目する桁の数値が、一つ前の桁の数値よりも小さい時
        ans += cur + 10 - pre  # 回転した値との差が押した回数となる
        pre = cur  # 一つ前の桁の数値を更新

# ボタンAを押した回数を加算
ans += len(Sr)
print(ans)

"""
法則を見つける系
一つ前の桁との差を見て、ボタンを押した回数を求める。
回転も考慮する。

https://atcoder.jp/contests/abc407/tasks/abc407_c/editorial
"""
