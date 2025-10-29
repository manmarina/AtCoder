N = int(input())
for i in range(1, 1000001):
    if int(str(i) * 2) > N:  # 文字列に変換して繰り返してから整数に戻す
        print(i - 1)  # Nを超える手前までの数が整数xの個数
        exit()

"""
問題を言い換える系
解説
https://atcoder.jp/contests/abc196/editorial/946
けんちょんよりもシンプルなコード。
ロジックはけんちょんと同じ。

たとえば 1234512345 は「良い整数」だが、これは「12345」という整数と同一視できる。
このように圧縮した整数の方を全探索すればよいことに気づく。

https://atcoder.jp/contests/abc196/tasks/abc196_c
"""
