from collections import defaultdict


N = int(input())
S = input()

if N == 1:  # N=1のとき1を表示して早期終了
    print(1)
    exit()

cnt = 1
dd = defaultdict(int)

for i in range(1, len(S)):  # ひとつ前の文字と比較
    pre = S[i - 1]
    cur = S[i]
    if pre == cur:  # 一緒ならカウントを増やす
        cnt += 1
    else:  # 違ったら、ddに格納したカウントと比較して、より大きければ更新
        dd[pre] = max(dd[pre], cnt)
        cnt = 1

# 最後の文字
last = S[-1]  # forループでは最後の文字の分が更新されないので
dd[last] = max(dd[last], cnt)  # ddに格納したカウントと比較して、より大きければ更新

# print(dd)
print(sum(v for v in dd.values()))

"""
自力解
ランレングス圧縮を意識せずに自力実装

https://atcoder.jp/contests/abc329/tasks/abc329_c
"""
