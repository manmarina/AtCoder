import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
Q = int(input())

# アルファベットの変換テーブル（クエリ処理の結果、各文字が何に変化するのかを記録）
convert = list(range(26))

for _ in range(Q):
    c, d = input().split()
    c = ord(c) - 97
    d = ord(d) - 97
    for i in range(26):  # 変換テーブルを走査
        if convert[i] == c:  # cなら
            convert[i] = d  # dに書き換える

res = [chr(convert[ord(ch) - 97] + 97) for ch in S]  # 変換テーブルに従って変換
print("".join(res))

"""
計算量を削減したクエリ処理
けんちょん
https://drken1215.hatenablog.com/entry/2024/11/23/115028
文字列そのものをいじるんじゃなくて、アルファベット26文字に対する“変換表”を作成する。

https://atcoder.jp/contests/abc342/tasks/abc342_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692e4ccd-42b8-8324-8783-c3f5635a42e5
"""
