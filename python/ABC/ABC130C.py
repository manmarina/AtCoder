W, H, x, y = map(int, input().split())

# 面積の半分（double 相当）
res = W * H / 2

# 結果表示（小数点以下10桁）
print(f"{res:.10f} ", end="")

# 中心判定（整数比較）
if x * 2 == W and y * 2 == H:  # (x,y)が中心なら
    print(1)  # 達成方法が無限に存在
else:  # (x,y)が中心でないときは
    print(0)  # (x,y)と中心を通る1通りのみ

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2019/06/17/003300
面積の大きくない方の面積の最大値は長方形の面積の1/2。
(x,y)と(W/2,H/2)を通る直線は、長方形の面積を2等分する。

https://atcoder.jp/contests/abc130/tasks/abc130_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915f546-c5b8-8322-8f7e-8c440e8a7b43
"""
