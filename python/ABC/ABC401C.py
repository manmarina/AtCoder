n, k = map(int, input().split())
s = k  # k個の和（初期値は1*k）
a = [1 for i in range(n + 1)]  # すべて1で初期化（i=Kまですべて1という初期条件）
# print(a)

for i in range(k, n + 1):  # kからスタート
    a[i] = s  # i=k以降のAiは、以前のk個の和

    # Sを更新
    s -= a[i - k]  # 一番古い値を引く
    s += a[i]  # 一番あたらしい値を足す
    s %= 1000000000  # 余りを取る
print(a[n])
# print(a)

"""
計算量を削減したシミュレーション
解説
https://atcoder.jp/contests/abc401/editorial/12689
愚直に毎回 Aiを求めると O(NK) かかってしまい実行時間制限に間に合いません。
ここで、Sをデータとして保持することにして、S を適宜更新することを考えます。

https://atcoder.jp/contests/abc401/tasks/abc401_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69042c33-f098-8323-a7d9-bc1ce4bfe36e
"""
