N, K = map(int, input().split())

res = 0.0
for n in range(1, N + 1):
    tmp = 1.0
    nn = n
    while nn < K:  # nnがKを超えない間
        nn *= 2
        tmp /= 2.0  # tmpを2で割り続ける
    res += tmp

res /= N
print(f"{res:.10f}")

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2019/05/19/224500_2
入力例1の解説どおりに確率を求める問題。
logを使わない実装。

https://atcoder.jp/contests/abc126/tasks/abc126_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
