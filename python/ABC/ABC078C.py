N, M = map(int, input().split())

teisyutu_kaisuu = 1 << M  # 1LL << M と同じ（2のM乗）
each_time = 1900 * M + 100 * (N - M)  # 提出1回あたりの実行時間

print(each_time * teisyutu_kaisuu)

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2019/03/23/175300
確率 pで成功するミッションを成功するまでトライし続けたとき、トライすることになる回数の期待値は 1/pである。

https://atcoder.jp/contests/abc078/tasks/arc085_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69141dbc-ad50-8320-b89d-8bbf2f5ac143
"""
