N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort(reverse=True)  # 体力が大きい順に必殺技を使いたい
# print(H)

print(sum(H[K:]))  # 必殺技以外の攻撃回数

"""
貪欲法

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/01/26/224100
素朴に考えれば、Hが大きい順に 0 にしていくと良さそうである。
    Hが大きい順にソートする
    大きい順に K個を 0 にする
    残った値の和を求める

https://atcoder.jp/contests/abc153/tasks/abc153_c
"""
