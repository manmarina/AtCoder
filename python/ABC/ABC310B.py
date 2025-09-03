from itertools import permutations
from multiprocessing.connection import answer_challenge

N, M = map(int, input().split())
PCF = [list(map(int, input().split()))for _ in range(N)]

# print(PCF)

for pi, pj in permutations(PCF, 2):
    Fi = set(pi[2:])
    Fj = set(pj[2:])
    # 条件を問題文通りにokとして実装
    ok = (pi[0] >= pj[0] and
          Fi <= Fj and
          (pi[0] > pj[0] or Fi < Fj))
    if ok:
        print("Yes")
        break
else:
    print("No")
