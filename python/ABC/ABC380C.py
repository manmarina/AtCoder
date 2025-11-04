N, K = map(int, input().split())
S = input()

# ランレングス圧縮
lens = []
i = 0
while i < N:
    j = i
    while j < N and S[j] == S[i]:
        j += 1
    lens.append((int(S[i]), j - i))  # (文字,文字長)を記録
    i = j
# print(lens)

# K 番目の 1 の塊を K−1 番目の 1 の塊の直後まで移動
num = 0
for i in range(len(lens)):
    if lens[i][0] == 1:  # 文字が1なら
        num += 1  # 1のカウントを増やす
        if num == K - 1 and i + 2 < len(lens):  # numがK-1の時
            # 右隣ともうひとつ右隣をスワップする
            lens[i + 1], lens[i + 2] = lens[i + 2], lens[i + 1]
# print(lens)

# 解凍して出力
for val, cnt in lens:
    print(str(val) * cnt, end="")
print()

"""
ランレングス圧縮
ランレングス圧縮した列上で、K番目の「1 の塊」と、その左の「0 の塊」を swap すればよい。

けんちょん
https://drken1215.hatenablog.com/entry/2024/11/17/012903

https://atcoder.jp/contests/abc380/tasks/abc380_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
