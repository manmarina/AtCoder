MOD = 10**9 + 7

N = int(input())
# 全体 - 0が存在しない場合 - 9が存在しない場合 + 0と9両方存在しない場合
ans = (pow(10, N, MOD) - 2 * pow(9, N, MOD) + pow(8, N, MOD)) % MOD
print(ans)

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2020/10/09/162600
包除原理で解ける問題。
けんちょんの解説の図がわかりやすい。

https://atcoder.jp/contests/abc178/tasks/abc178_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6916d56d-47d8-8321-88cc-45996e7c90e1
"""
