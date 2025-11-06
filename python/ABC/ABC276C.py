def prev_permutation(seq):
    """seq を直前の順列に書き換え、存在すれば True を返す。なければ False。"""
    a = list(seq)
    i = len(a) - 1
    while i > 0 and a[i - 1] < a[i]:
        i -= 1
    if i <= 0:
        return False, a

    j = len(a) - 1
    while a[j] >= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = reversed(a[i:])
    return True, a


def next_permutation(seq):
    """seq を直後の順列に書き換え、存在すれば True を返す。なければ False。"""
    a = list(seq)
    i = len(a) - 1
    while i > 0 and a[i - 1] > a[i]:
        i -= 1
    if i <= 0:
        return False, a

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]
    a[i:] = reversed(a[i:])
    return True, a


N = int(input())
P = list(map(int, input().split()))

ok, prev = prev_permutation(P)
print(*prev)

"""
ライブラリ関数を活用する系
ライブラリ関数がないので、チャッピーに作ってもらった関数を利用。
ロジックは理解していない。
次の順列を返す関数も作ってくれた！

https://atcoder.jp/contests/abc276/tasks/abc276_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c18f0-1cc0-8323-a3f8-e87a81738bce
"""
