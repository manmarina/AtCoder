from itertools import permutations


S, K = input().split()
K = int(K)

ans = set()
for perm in permutations(S, len(S)):
    ans.add(''.join(perm))

ans = sorted(ans)
# print(ans)
print(ans[K - 1])

"""
順列全探索
自力解

重複文字を含む文字列 S の順列を辞書順（lexicographic）に並べ、K 番目を出力する問題です。
"""
