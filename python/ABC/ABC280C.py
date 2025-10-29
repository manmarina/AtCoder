S = input()
T = input()

for i in range(len(S)):
    if S[i] != T[i]:
        print(i + 1)  # 文字が異なる最初の位置を出力して終了
        exit()

print(len(T))  # 挿入位置が最後だった場合

"""
文字列操作

けんちょんの解説
https://drken1215.hatenablog.com/entry/2022/12/06/174000
深く考えずに for 文回した人も多いと思う。実際それでも問題なく解ける！

https://atcoder.jp/contests/abc280/tasks/abc280_c
"""
