N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

# 総時間 T
T = sum(a / b for a, b in AB)
half = T / 2.0

acc_time = 0.0   # これまでに左から燃やした時間
acc_len = 0.0   # これまでに完全に燃えた長さ

for a, b in AB:
    t = a / b
    if acc_time + t < half:  # T/2を過ぎない時
        acc_time += t  # 燃やした時間を増やす
        acc_len += a  # 燃えた長さを増やす
    else:  # T/2を過ぎた時
        rem = half - acc_time      # この区間で消費する残り時間
        acc_len += rem * b         # その時間で進む長さ
        print(acc_len)
        break

"""
問題を言い換える系
チャッピー

「時間の累積」で片側からシミュレーション
左右から同時に火をつけたときに“左側の火がちょうど半分の時間で到達する位置”を求める問題と言い換える。

要点（アルゴリズムの核心）
左右から同じ時刻 T/2 まで燃やしたところでちょうど出会います（対称性）。

よって「左から時間を積み上げて、累積時間が T/2 になる位置」を求めれば、その位置が答えです。
"""
