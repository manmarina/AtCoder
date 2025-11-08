N = input()

lenN = len(N)
cand = []  # 候補を格納

# ビット全探索して、ある桁を削除
for mask in range(1, 1 << lenN):
    num = []
    for i in range(lenN):
        if (mask >> i) & 1:
            num.append(N[i])
    cand.append(int(''.join(num)))  # 候補を数値に変換して格納
# print(cand)

# 各候補が3の倍数かどうか調べる
ans = 18
for c in cand:
    if c % 3 == 0:  # 3の倍数の時
        ans = min(ans, lenN - len(str(c)))  # 削除した桁数が最小なら更新
print(ans if ans != 18 else -1)  # 3の倍数にできないときは-1

"""
ビット全探索（bit全探索）
どの桁を除去するのかをビット全探索する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/11/30/014517

https://atcoder.jp/contests/abc182/tasks/abc182_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690f60b5-7d3c-8321-b448-8b1027b2acff
"""
