from itertools import product


N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

ans = []


def dfs(curr, count):  # (文字列,結合回数)
    # count 個の文字列を結合して curr になった状態
    if count == K:  # 結合回数がK回になったら
        ans.append(curr)  # リストに文字列を追加
        return
    for s in S:  # S から一つずつ取り出して再帰dfs
        dfs(curr + s, count + 1)  # (文字列を連結、結合回数を+1)


dfs("", 0)  # (空文字、count=0)からスタート
ans.sort()  # リストを昇順ソート
print(ans[X - 1])  # 辞書順でX番目を表示

"""
全探索 + dfs
組み合わせ生成にdfsを使用
各頂点にN個の文字列いずれかが書かれた、""を根とする高さKのN分木を考える
https://yuulis.hatenablog.com/entry/ABC-416-C
https://atcoder.jp/contests/abc416/editorial/13535

https://atcoder.jp/contests/abc416/tasks/abc416_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
