S1 = list(map(int, input()))
# print(S1)

S2 = S1.copy()  # 2解試すのでコピーしておく

# 1パターン目
cnt1 = 0
for i in range(1, len(S1)):
    if S1[i] == S1[i - 1]:  # 前の文字と同じなら反転
        S1[i] = S1[i] ^ 1
        cnt1 += 1  # 反転したらカウントを増やす
# print(S1, cnt1)

# 2パターン目
S2[0] = S2[0] ^ 1  # 先頭を反転させておく
cnt2 = 1
for i in range(1, len(S2)):
    if S2[i] == S2[i - 1]:  # 前の文字と同じなら反転
        S2[i] = S2[i] ^ 1
        cnt2 += 1  # 反転したらカウントを増やす
# print(S2, cnt2)

print(min(cnt1, cnt2))

"""
文字列操作

https://atcoder.jp/contests/abc124/tasks/abc124_c
https://blog.hamayanhamayan.com/entry/2019/04/14/001053
"""
