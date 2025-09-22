X = input().strip()
N = int(input())
S = [input().strip() for _ in range(N)]

rank = {c: i for i, c in enumerate(X)}  # 文字→順位


def key_by_rank(s: str):
    return tuple(rank[c] for c in s)


S.sort(key=key_by_rank)  # 自作関数をキーに利用（文字列をインデックスのタプルに変換）
print(*S, sep='\n')

"""
文字列操作
チャッピー

与えられたアルファベット順（X）に従って、N 個の小文字文字列を辞書順ソートする問題です。
通常の a-z ではなく、X の並びを“あたらしい辞書順”として使います。

必要なテクニック
文字のランク化（写像作成）
    rank[c] = X における c の位置(0..25) という辞書を作る。
    これで任意の文字列 s を「ランク列」や「通常 a-z に戻した文字列」に変換できる。

キー関数によるソート
    Python なら sorted(words, key=transform) の transform を自作する。
    文字ごとに rank[c] を並べたタプル/リストや、a..z に再マッピングした文字列をキーにする。

“座標圧縮”に似た発想
    元の値（文字）→ 連番（0..25）に落とすという意味で、考え方は座標圧縮と同型です。
"""
