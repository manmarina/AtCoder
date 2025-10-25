from collections import defaultdict

import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


N = int(input())

beans = defaultdict(list)  # key=色、values=おいしさのリスト
for _ in range(N):
    a, c = map(int, input().split())
    beans[c].append(a)
logging.debug(f"{beans = }")

ans = max(min(v) for v in beans.values())  # おいしさのリストの最小値を比較して最大のものが答え
print(ans)


"""
基本実装問題
おいしさのリストの最小値を比較して最大のものが答え

https://chatgpt.com/c/68fc9e38-990c-8322-95bb-e1b8e2a7581e
https://atcoder.jp/contests/abc348/tasks/abc348_c
"""
