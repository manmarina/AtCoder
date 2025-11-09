N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    T += (h // 5) * 3  # 3回の攻撃で5削る
    h %= 5  # 3回1セットの攻撃の後に残った体力（0~4)

    while h > 0:  # まだ体力があれば
        T += 1  # 攻撃する
        if T % 3 == 0:  # 3の倍数のとき
            h -= 3  # 3削る
        else:  # そうでなければ
            h -= 1  # 1削る

print(T)

"""
計算量を削減したシミュレーション
完全な愚直シミュレーションでは TLEしてしまう。
「どの位置からスタートしても3回攻撃したら合計5ダメージになる」という周期性を見抜く。

けんちょん
https://drken1215.hatenablog.com/entry/2024/08/30/015445

http://atcoder.jp/contests/abc368/tasks/abc368_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691006bf-367c-8321-a12b-96796ad1c25f
"""
