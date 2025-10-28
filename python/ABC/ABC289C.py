n, m = map(int, input().split())
a = [[] for i in range(m)]
for i in range(m):
    _ = int(input())
    a[i] = list(map(int, input().split()))
# print(a)

result = 0
for bit in range(1 << m):  # bit全探索
    s = set()  # 重複排除のためsetを使用
    for i in range(m):
        # if bit & (1 << i) != 0:
        if (bit >> i) & 1 != 0:
            for j in a[i]:
                s.add(j)  # bitが立っている集合の要素をsetに追加
    if len(s) == n:  # 要素数がnなら
        result += 1  # カウントを増やす

print(result)


"""
ビット全探索（bit全探索）
プロひろ
https://programming-hiroba.com/abc289-c/
集合の選び化をbit全探索。
選んだ集合を合わせた中に、1~Nまですべての数字が入っているものをカウントする。

https://qiita.com/Rasukaru-raccoon/items/87103d6e056d9bc4aa20
"""
