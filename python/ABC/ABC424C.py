from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = [0] * (N + 1)  # 1- indexに変換して格納
B = [0] * (N + 1)  # 1- indexに変換して格納

starters = []  # (0,0)の位置を1-indexで格納（qの初期値として使用）
for i in range(1, N + 1):
    a, b = map(int, input().split())
    A[i], B[i] = a, b
    if a == 0 and b == 0:
        starters.append(i)
# print(A)
# print(B)
# print(starters)

# グラフ作成
# 逆隣接：自身を参照しているインデックスを格納してゆく
children = [[] for _ in range(N + 1)]
for i in range(1, N + 1):  # 値とインデックスを逆にして格納するところがポイント!!
    if A[i] != 0:
        children[A[i]].append(i)  # インデックス2->値1　を　インデックス1->値2で格納
    if B[i] != 0:
        children[B[i]].append(i)  # インデックス2->値1　を　インデックス1->値2で格納
# print(children)

# BFS部分
seen = [False] * (N + 1)

for s in starters:  # 全ての（0，0）のseenをTrueにする
    seen[s] = True
q = deque(starters)  # 全ての（0，0）dequeに格納する=多点始点BFS
while q:
    u = q.popleft()
    for v in children[u]:
        if not seen[v]:
            seen[v] = True   # 親のどちらかが習得済みになった時点で習得
            q.append(v)
# print(seen)

print(sum(seen))

"""
多点始点BFS（逆隣接グラフを使用）
チャッピー

ざっくり言うと「最初に習得済み（Ai,Bi)=(0,0) のスキルから始めて、
そこから“親のどちらかを習得していれば解放される矢印を伝播していく
reachability（到達可能性）判定」です。
問題の本質はグラフ化 + 多点BFS/DFS で OK


ポイントと手順
グラフ化（逆隣接リスト）
    各スキル i には条件 (Ai, Bi) が付きます。
    「Ai を覚えると i が解放候補」「Bi を覚えると i が解放候補」と見なして、
    children[Ai].append(i), children[Bi].append(i) を作ります（Ai==Bi でも問題なし）。

多点スタート
    (Ai,Bi)=(0,0) の i たちが最初から「習得済み」。
    これらを 全てキュー（またはスタック）に入れて 伝播開始。

伝播（BFS/DFS）
    キューから取り出した習得済みノード u について、children[u] の各 v を見て
    「v が未習得なら習得にする → キューへ」。
    条件は“親のどちらかが習得済み”なので、最初に一度でも親から触れられた時点で習得可。
    二度目以降は無視（visited で管理）。

カウント
    visited の個数が答え。計算量は O(N)（辺は最大 2N 程度）。

つまずきポイント・注意
    (0,0) が一つもないと初期習得がゼロなので、何も始まらず答えは 0。
    自己ループ/Ai=Bi でも visited 管理があるのでそのままでよい（重複登録しても再訪しない）。
    入力は 1-indexed。children などの配列も 1..N を素直に持つとミスが減ります。
    再帰DFSでも書けますが、N=2e5 なので Python は BFS（反復）推奨。
"""
