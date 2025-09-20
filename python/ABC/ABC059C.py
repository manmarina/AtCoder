import sys


def cost_with_pattern(a, first_positive: bool) -> int:
    s = 0
    cost = 0
    for i, x in enumerate(a, start=1):
        s += x
        # その位置で正が必要か？
        need_pos = (i % 2 == 1) if first_positive else (i % 2 == 0)
        if need_pos:
            if s <= 0:
                add = 1 - s   # sを+1へ
                cost += abs(add)
                s = 1
        else:
            if s >= 0:
                add = -1 - s  # sを-1へ
                cost += abs(add)
                s = -1
    return cost


input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))

# 奇数番目を正、奇数番目を負の両パターン試して、低コストな方を答えとして出力する
ans = min(
    cost_with_pattern(a, first_positive=True),   # 奇数番目を正に
    cost_with_pattern(a, first_positive=False),  # 奇数番目を負に
)

print(ans)

"""
prefix和（累積和とは異なる）
チャッピー

配列の各要素に±1の操作を好きなだけ行って、すべてのprefix和 が 0 にならないようにし、
さらに 正負が交互になるように最小コストで調整する、という内容です。

ちなみに
    prefix和 = その時点までの合計（数式）
    累積和 = prefix和を全部並べた配列（プログラム上のテクニック）
"""
