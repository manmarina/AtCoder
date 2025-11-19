N, A, B = map(int, input().split())
S = input()

ans = 10**18  # 最大値はもっと大きい可能性もあるがこれでACできた
for i in range(N):  # 文字の移動を全パターン試す
    ng = 0
    for j in range(N // 2):  # 回文判定
        # print(S[(j + i) % N], S[(N - 1 - j + i) % N])
        if S[(j + i) % N] != S[(N - 1 - j + i) % N]:  # 対応する文字が一致しない時
            ng += 1  # カウントを増やす
    ans = min(ans, B * ng + A * i)  # 回文にするためのコストが最小なら更新

print(ans)

"""
全探索
全探索するが、回文判定を高速に行えるように、配列は変更せずに、インデックスをシフトする。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/01/29/201129

https://atcoder.jp/contests/abc286/tasks/abc286_c
"""
