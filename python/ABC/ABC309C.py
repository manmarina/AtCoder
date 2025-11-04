N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()
# print("AB:", AB)
pills = sum(b for _, b in AB)
# print("pills:", pills)

if pills <= K:
    print(1)
    exit()

for a, b in AB:
    pills -= b
    if pills <= K:
        print(a + 1)
        break

"""
シミュレーション系
aiの値が小さい順にイベントを並び替える。なお、このような考え方をイベントソートと呼ぶ。
イベントをソートした順に処理していき、はじめて K錠以下になる瞬間を捉えればよい。

けんちょん解説
https://drken1215.hatenablog.com/entry/2024/06/01/030100

https://atcoder.jp/contests/abc309/tasks/abc309_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690969e4-f840-8324-ad40-0f302fa139c8
"""
