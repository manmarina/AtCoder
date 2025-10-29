import sys
sys.setrecursionlimit(10**7)


def dfs(A, K, R, s):  # s=Aの総和
    # 終端条件 --- N 個そろったら判定して出力
    if len(A) == len(R):
        if s % K == 0:  # 総和がKの倍数の時
            print(*A)  # 結果を出力
        return

    idx = len(A)  # いま何番目を決めているか
    for v in range(1, R[idx] + 1):
        A.append(v)
        dfs(A, K, R, s + v)
        A.pop()  # 戻すのが大事（バックトラック）


N, K = map(int, input().split())
R = list(map(int, input().split()))

dfs([], K, R, 0)  # Aの総和=0

"""
再帰DFSによる全探索
n重for文の全探索に再帰DFSを応用
けんちょん
https://drken1215.hatenablog.com/entry/2024/08/20/224513
n重for文の全探索に再帰DFSを応用する方法の詳しい解説
https://drken1215.hatenablog.com/entry/2020/05/04/190252

https://atcoder.jp/contests/abc367/tasks/abc367_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690188f5-ed80-8321-9d70-4b573ac905a8
"""
