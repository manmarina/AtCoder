from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

"""
itertools.permutations は「入力の並び順に対する辞書順」で生成します。
だから range(1, N+1) のように昇順で一意な要素を渡せば、
そのまま通常の辞書順（昇順の辞書順）になります。リストに溜めてソートし直す必要はありません。
"""
idxP = idxQ = None
for i, perm in enumerate(permutations(range(1, N + 1))):
    if perm == P:
        idxP = i
    if perm == Q:
        idxQ = i
    if idxP is not None and idxQ is not None:
        break
print(abs(idxP - idxQ))

"""
順列全探索（itertools.permutations）

発想：全ての順列を辞書順で生成して、PとQが何番目か（0/1始まりに注意）を数える。
計算量：O(N!·N) ただし N≤8 なので余裕。
実装ポイント：
    for i, perm in enumerate(permutations(range(1, N+1))):
    PとQを見つけたらそのインデックスを記録して差を出す。
    途中で両方見つかったらループを抜けてOK。
"""
