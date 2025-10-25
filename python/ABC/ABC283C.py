S = input()

N = len(S)
is_zero = False
cnt = 0
for i in range(N):
    cnt += 1
    if S[i] == '0' and is_zero:  # 0が2つ並んだとき
        is_zero = False
        cnt -= 1  # カウントを1つ減らす
    elif S[i] == '0' and not is_zero:  # 0が奇数個目のとき
        is_zero = True
    else:
        is_zero = False
print(cnt)

"""
シミュレーション系

テンキーの入力回数カウント。
00のときは1とカウントする。

https://atcoder.jp/contests/abc283/tasks/abc283_c
"""
