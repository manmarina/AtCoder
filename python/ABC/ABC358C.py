N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = []
for mask in range(1 << N):  # ビットマスク生成
    # print(bin(mask))
    type = set()  # ポップコーンの種類数を判定するset
    cnt = 0  # 売り場を組み合わせた数
    for i in range(N):
        if (mask >> i) & 1:  # ビットマスクが立っていたら
            cnt += 1  # 売り場の数を+1
            for j in range(M):
                if S[i][j] == 'o':
                    type.add(j)  # ポップコーンの種類をtypeに追加
    if len(type) == M:  # ポップコーンが全種類買えたら
        ans.append(cnt)  # 売り場の数をansに保存

print(min(ans))  # 最も少ない売り場の数を出力

"""
ビット全探索（bit全探索）
全ての売り場の組み合わせをビット全探索する。
全種類買えた組み合わせで、最も少ない売り場の数を出力する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/07/07/214839

https://atcoder.jp/contests/abc358/tasks/abc358_c
"""
