H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


def pick_indices(mask, n):              # mask で立っているビットの添字を昇順で返す
    return [i for i in range(n) if (mask >> i) & 1]


for rmask in range(1 << H1):
    if rmask.bit_count() != H2:         # ちょうど H2 行だけ残す
        continue
    rows = pick_indices(rmask, H1)

    for cmask in range(1 << W1):
        if cmask.bit_count() != W2:     # ちょうど W2 列だけ残す
            continue
        cols = pick_indices(cmask, W1)

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
部分集合列挙（ビット全探索(bit全探索)）
チャッピー

A から 行を H2 本、列を W2 本だけ選んでできる「順序を保った部分行列」が B と一致するかを調べる

https://atcoder.jp/contests/abc264/tasks/abc264_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df3a66-613c-8322-884d-4ff40066eb00
"""
