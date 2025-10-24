N, T = map(int, input().split())
As = list(map(int, input().split()))

# 各行・各列・斜め方向の、穴の空いた集合を管理する
# lines[0..N-1]        : 各行
# lines[N..2N-1]       : 各列
# lines[2N]            : 左上→右下の斜め
# lines[2N+1]          : 右上→左下の斜め
lines = [set() for _ in range(N * 2 + 2)]


def play(line_id, val, turn):
    lines[line_id].add(val)  # bingoカードに穴を開ける

    if len(lines[line_id]) >= N:  # このラインで穴がN個空いたら
        print(turn)

        # print(lines)
        exit()


# Tターン分の入力を読む
for turn in range(1, T + 1):
    A = As[turn - 1]
    x = (A - 1) // N  # Aの値をx座標に変換
    y = (A - 1) % N  # Aの値をy座標に変換

    # linesは(行、列、左上→右下 の斜め,右上→左下 の斜め)の順で格納されている
    # 制約より、Ai<=N^2なので、必ずどこかに格納できる
    # 行 x
    play(x, A, turn)  # xはlinesの格納位置

    # 列 y
    play(N + y, A, turn)  # N+yはlinesの格納位置

    # 左上→右下 の斜め
    if x == y:
        play(2 * N, A, turn)  # 2*xはlinesの格納位置

    # 右上→左下 の斜め
    if x + y == N - 1:
        play(2 * N + 1, A, turn)  # 2*x+1はlinesの格納位置

# ビンゴしなかった場合
print(-1)
# print(lines)

"""
計算量を削減したシミュレーション

けんちょん
https://drken1215.hatenablog.com/entry/2024/07/08/004128
ビンゴしたかどうかO(1)で確認できる判定用のsetを8ライン分作成
ターンごとにラインに数字を追加してゆき、setの長さがNに達したらビンゴ

初期化 O(N) + メインループ O(T)
-> 合わせて 時間計算量は O(N + T) に改善

https://atcoder.jp/contests/abc355/tasks/abc355_c
https://chatgpt.com/c/68fb2c1f-c294-8323-beed-4683776be355
"""
