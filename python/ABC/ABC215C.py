def next_permutation(a):
    """
    C++ の std::next_permutation と同じ自作関数
    「リストを1回呼び出すたびに次の順列に更新」してくれるユーティリティ
    使えれば良いと思うので中身は理解していない。
    必要なときに引用しよう！

    a はリスト（例: ['a','a','b'] や [1,2,3]）。
    **「辞書順で次の順列」**とは：
    例） [1,2,3] → [1,3,2] → [2,1,3] → [2,3,1] → [3,1,2] → [3,2,1]
    最後の [3,2,1] に到達したときは「次が存在しない」ので False を返す。
    それ以外は True を返して、リスト a を「次の順列」に更新する。
    """
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True


S, K = input().split()
K = int(K)

S = [*S]
S.sort()
for _ in range(K - 1):
    next_permutation(S)   # Sを重複なしで次の辞書順に更新する
    # print(''.join(S))
print(''.join(S))

"""
next_permutationが学べる良問 回答が得られるまで順列列挙
チャッピー

next_permutationを使うので効率的
    全列挙しなくて良い
    実行回数はK-1回のみ（実行前のソートが1回分に相当するため）

重複文字を含む文字列 S の順列を辞書順（lexicographic）に並べ、K 番目を出力する問題です。

辞書順の列挙（next_permutation）
文字列をソートしてから next_permutation を繰り返すと、重複を含んでいても辞書順に重複なしで全順列を列挙できます。
N ≤ 8 なので最悪でも 8! = 40320 通り、全列挙で余裕です。
C++ なら std::next_permutation、Python なら自作（数行）でOK。

重複除去の正攻法
itertools.permutations(S) をそのまま使うと重複が出ることがあります。
ソート+next_permutation か、あるいは多重集合カウント法を使いましょう。
どうしても全列挙したい場合は sorted(set(permutations(S))) でも通ります（N ≤ 8 なので可）。
"""
