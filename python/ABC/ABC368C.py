N = int(input())
H = list(map(int, input().split()))

T = 0
for i in range(N):
    h = H[i]
    T += h // 5 * 3

    res = h % 5
    while res > 0:
        T += 1
        if T % 3 == 0:
            res -= 3
        else:
            res -= 1

print(T)

"""
計算量を削減したシミュレーション
リトライ

完全な愚直シミュレーションでは TLEしてしまう。
「どの位置からスタートしても3回攻撃したら合計5ダメージになる」という周期性を見抜く。
けんちょんと同じロジックで実装できた！

けんちょん
https://drken1215.hatenablog.com/entry/2024/08/30/015445

http://atcoder.jp/contests/abc368/tasks/abc368_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691006bf-367c-8321-a12b-96796ad1c25f
"""
