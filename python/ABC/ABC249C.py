import sys


input = sys.stdin.readline
N, K = map(int, input().split())
S = [input().strip() for _ in range(N)]

ans = 0
for mask in range(1 << N):
    cnt = [0] * 26  # a..z
    for i in range(N):
        if (mask >> i) & 1:
            # 同じ文字は1つの文字列内では1回として数える
            for ch in set(S[i]):
                cnt[ord(ch) - 97] += 1
    # ちょうど K 個の文字列に含まれる文字の個数
    score = sum(1 for x in cnt if x == K)
    ans = max(ans, score)

print(ans)

"""
ビット全探索
チャッピー

bit全探索（部分集合列挙）+文字頻度カウント

https://atcoder.jp/contests/abc249/tasks/abc249_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dd42c2-9f10-8331-bb85-b6458b01f13c
"""
