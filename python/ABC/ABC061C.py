N, K = map(int, input().split())
ab = [tuple(map(int, input().split()))for _ in range(N)]
# print(ab)

# abをaをキーに昇順でソートしておく
ab.sort(key=lambda x: x[0])

cs = 0
for a, b in ab:
    cs += b
    if cs >= K:  # b の累積和がKを超えた時 a を表示して終了
        print(a)
        break

"""
累積和（prefix和）
自力解

 狙いはシンプルです：
巨大配列を作る代わりに、
値で昇順ソート → 累積和が K に届いた瞬間の値を答える、これだけです。

この問題の注意点として、Sを具体的に作ろうとすると、最大で
10**10くらいのサイズになってメモリも計算時間も飛んでしまうので注意。。。
"""
