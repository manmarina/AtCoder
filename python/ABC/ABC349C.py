S = input()
T = input()

t = T.lower()  # 小文字に変換
i = 0
for s in S:  # sを先頭文字から探索
    if s == t[i]:  # t[0] から一致を見る 一致していたら1文字進める
        if i == 2:  # 3文字とも一致したら終了
            print("Yes")
            exit()
        i += 1

    if t[-1] == 'x' and i == 2:  # 先頭2文字が一致していて、tの末尾が'x'なら終了
        print("Yes")
        exit()

print("No")

"""
文字列操作
ルール通りに短縮された文字かどうか判定する

https://atcoder.jp/contests/abc349/tasks/abc349_c
"""
