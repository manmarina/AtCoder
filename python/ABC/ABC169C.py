A, B = input().split()
A = int(A)
B = int(B.replace('.', ''))  # '.'を省いて整数に変換（100倍）

print(A * B // 100)  # Bは小数第2位と決まっているので

"""
数学的な気づき系
小数点以下の切り捨てに関する問題。
math.floorでは、誤差が原因になってWAしてしまうので、すべて整数演算で行う。

けんちょんの
https://drken1215.hatenablog.com/entry/2020/05/31/224300

https://atcoder.jp/contests/abc169/submissions/70914681
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6916af07-5258-8324-9764-240305ce4c6f
"""
