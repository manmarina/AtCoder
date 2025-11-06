from itertools import combinations


a, b, c, d, e = map(int, input().split())

# 名前の作成と点数計算を同時に行う
ABCDE = ['A', 'B', 'C', 'D', 'E']
member = []
for i in range(1, 5 + 1):
    for combi in combinations(ABCDE, i):  # 5C1 ~ 5C5まで
        point = 0
        for ch in combi:  # 名前のリストから1文字取り出して、加点する
            if ch == 'A':
                point += a
            elif ch == 'B':
                point += b
            elif ch == 'C':
                point += c
            elif ch == 'D':
                point += d
            else:  # c == 'E':
                point += e

        member.append((point, ''.join(combi)))  # (点数,名前)のタプルを格納

member.sort(key=lambda x: (-x[0], x[1]))  # 点数降順、名前昇順でソート
# print(member)
print(*[name for _, name in member], sep='\n')  # 名前だけ出力

"""
基本実装問題
名前の生成とソートが鍵となる。

https://atcoder.jp/contests/abc384/tasks/abc384_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690bfcef-47e4-8321-9e44-610d44a69b9c
"""
