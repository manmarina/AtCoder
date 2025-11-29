N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]


res = []

for i, s in enumerate(S):
    # 文字数差が 2 以上なら必ずダメ
    if abs(len(s) - len(T)) >= 2:
        continue

    # 先頭から一致している文字数 pre
    pre = 0
    lim = min(len(s), len(T))
    while pre < lim and s[pre] == T[pre]:
        pre += 1

    # 末尾から一致している文字数 suf
    suf = 0
    while suf < lim and s[len(s) - 1 - suf] == T[len(T) - 1 - suf]:
        suf += 1

    # 条件チェック
    # S=Tの時, Sに1文字挿入してTになる時, Sの1文字削除でTになる時
    if pre + suf >= min(len(s), len(T)):
        res.append(i + 1)  # 1-indexed
    # Sの1文字変更でTになる時
    elif len(s) == len(T) and pre + suf + 1 == len(s):
        res.append(i + 1)

print(len(res))
if res:
    print(*res)
else:
    print()  # 空行

"""
場合分け系
けんちょん
https://drken1215.hatenablog.com/entry/2023/10/21/185053
S_i の長さの 総和 も 5x10^5 以下なので各 S_i に対して O(|S_i|) ぐらいの処理ならギリギリOK

https://atcoder.jp/contests/abc324/tasks/abc324_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692ac386-3070-8324-b9c1-2e3f5ad9ba23
"""
