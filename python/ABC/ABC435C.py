N = int(input())
A = [0] + list(map(int, input().split()))
# print(A)

mx = 0
for i in range(1, N + 1):
    ikeru = i + A[i] - 1
    mx = max(mx, ikeru)
    if mx == i:
        print(i)
        exit()

print(N)

"""
シミュレーション
時間切れ
めちゃくちゃ簡単なのにACできなくて悔しい。
Aiごとに、どこまで倒せるかを計算して最大値を更新。
もし最大値がiと一致したときにはそこで終了。

https://atcoder.jp/contests/abc435/tasks/abc435_c
"""
