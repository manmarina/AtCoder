from itertools import combinations

H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for rows in combinations(range(H1), H2):      # 例: (0,2,4) のように昇順で返る → 順序維持OK
    for cols in combinations(range(W1), W2):  # 例: (1,3,5)
        ok = True
        for i in range(H2):
            for j in range(W2):
                if A[rows[i]][cols[j]] != B[i][j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print("Yes")
            exit()

print("No")

"""
部分集合列挙（組合せ列挙）
チャッピー

A から 行を H2 本、列を W2 本だけ選んでできる「順序を保った部分行列」が B と一致するかを調べる

https://atcoder.jp/contests/abc264/tasks/abc264_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df3a66-613c-8322-884d-4ff40066eb00
"""
