from collections import defaultdict
import sys


input = sys.stdin.readline
N = int(input())
S = input().strip()
W = list(map(int, input().split()))

adult = defaultdict(int)   # weight -> #adults (S[i]=='1')
child = defaultdict(int)   # weight -> #children (S[i]=='0')

for s, w in zip(S, W):
    if s == '1':
        adult[w] += 1
    else:
        child[w] += 1

cur = sum(adult.values())      # X を極小にしたとき = 全員「大人」判定
ans = cur  # 正しく判定できている大人の数をansの初期値に
print(adult)
print(adult.values())
print(cur)

for w in sorted(set(W)):  # しきい値をソートした体重リストの最小から最大へ変化
    # w をまたいだ瞬間の一括反転　しきい値をまたぐと子供は正しく判定され、大人は誤判定される
    cur += child[w] - adult[w]
    if cur > ans:
        ans = cur

print(ans)


"""
基本実装問題
チャッピー
ソート + スイープライン（しきい値を動かす）

しきい値 X を小さい方から大きい方へ動かすと、各重み w をまたぐ瞬間にだけ 判定が変わります。
X が極小のときは全員を「大人」と判定するので、初期正答数 = 実際の大人の人数。
X を w の直後へ超えると、重みちょうど w の人たちの判定が
    実際が子なら「誤→正」に +1
    実際が大人なら「正→誤」に -1
へ一括で反転。
これを重みごとにまとめて適用し、最大値を取ればよい。

https://atcoder.jp/contests/abc257/tasks/abc257_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de1bd9-24f4-8321-bbd1-47bf976c5864
"""
