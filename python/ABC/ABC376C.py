N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)  # 降順ソート（後ろから考える）
B.sort(reverse=True)  # 降順ソート（後ろから考える）
B.append(0)  # これがないと一番小さい箱を買うケースでREになる
# print(A)
# print(B)

shift = 0  # 箱を買ったときにBのインデクスをシフトする
flag = False  # 箱を買ったか？
for i in range(N):
    if A[i] > B[i - shift]:  # Aiのほうが大きい時
        if not flag:  # 箱を買っていない時、箱を買う
            shift = 1
            flag = True
            ans = A[i]
        else:  # すでに箱を買っていたら
            print("-1")
            exit()
print(ans)

"""
後ろから考える系
小さい方から考えると、ある箱に入らなかった時、箱を買うべきか、持っている箱から使うべきか判断が難しい。
大きい方から考えると、ある箱に入らなかったらその時点で買うしかない。
買ったのに全部入り切らなかったら-1、入りきったら買った箱の大きさを出力する。

https://atcoder.jp/contests/abc376/tasks/abc376_c
"""
