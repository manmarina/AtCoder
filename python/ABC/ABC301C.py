import string

# 入力
S = input()
T = input()
alpha_num_S, alpha_num_T = S.count('@'), T.count('@')
# print(alpha_num_S, alpha_num_T)

# 各文字 c = 'a', 'b', ..., 'z' に対して、S, T で共通の文字を対消滅させる
for c in string.ascii_lowercase:  # 'abcdefghijklmnopqrstuvwxyz'
    # S, T 中の文字 c の個数を数える
    c_num_S, c_num_T = S.count(c), T.count(c)
    # print(c_num_S, c_num_T)

    # もし S, T いずれかに文字が余ったとき、それが "atcoder" に含まれないとダメ
    if c_num_S != c_num_T and c not in "atcoder":
        print("No")
        exit()

    # S, T の文字 c を対消滅させて、残った個数分、文字 @ を削る
    if c_num_S > c_num_T:
        alpha_num_T -= (c_num_S - c_num_T)
    else:
        alpha_num_S -= (c_num_T - c_num_S)

    # 文字 @ が不足したらダメ
    if alpha_num_S < 0 or alpha_num_T < 0:
        print("No")
        exit()

print("Yes")

"""
文字列操作
アルファベット中のある文字cについて
S, T の文字数が同じとき、対消滅させる
S, T の文字数が異なったとき、"atcoder"に含まれなければ終了
S, T の文字数が異なったとき、異なった個数分、文字@を削る
文字@がマイナスになったら終了

けんちょん
https://drken1215.hatenablog.com/entry/2023/05/14/001500

https://atcoder.jp/contests/abc301/tasks/abc301_c
https://chatgpt.com/c/68faeca9-0284-8324-8756-ba29d3694c5a
"""
