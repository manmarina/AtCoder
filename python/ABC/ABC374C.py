N = int(input())
K = list(map(int, input().split()))

ans = 20 * 10**8
# 全て0にならないように1よりスタート
# 全て1にならないように(1 << k) - 1で終了
for mask in range(1, (1 << N) - 1):
    # print(f"{mask:0{N}b}")
    A, B = [], []
    for i in range(N):
        if (mask >> i) & 1:  # ビットが立っていたら
            A.append(K[i])  # Aに追加
        else:  # 立っていなければ
            B.append(K[i])  # Bに追加
    mx = max(sum(A), sum(B))  # 人数が多い方のグループの人数
    ans = min(ans, mx)  # 最小であれば更新

print(ans)

"""
ビット全探索（bit全探索）
グループ分けをビット全探索する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/10/06/030519

https://atcoder.jp/contests/abc374/tasks/abc374_c
"""
