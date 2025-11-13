import math

N, K = map(int, input().split())


ans = 0
for i in range(1, N + 1):  # すべてのサイコロの目
    if i >= K:  # 出目がK以上の時
        ans += 1  # 確率1を加算
    else:  # そうでないとき
        exp = math.ceil(math.log(K / i, 2))  # チャッピーの解説を参照
        ans += pow(0.5, exp)  # コインを振ってexp回連続で表が出る確率
print(ans / N)  # 総和を求めてからNで割っている


"""
数学的な気づき系
入力例1の解説どおりに確率を求める問題。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2019/05/19/224500_2

https://atcoder.jp/contests/abc126/tasks/abc126_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
