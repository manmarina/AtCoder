import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

Q = int(input())
min_h, max_h = [], []  # 最小値用のヒープと、最大値用のヒープを用意
cnt = defaultdict(int)  # ヒープの要素数をカウントする


def push(x):
    cnt[x] += 1
    heapq.heappush(min_h, x)
    heapq.heappush(max_h, -x)


def discard(x, c):
    if cnt[x] == 0:
        return
    d = min(cnt[x], c)
    cnt[x] -= d


def clean_min():
    # cntが0なのに、ピープの先頭に溜まったゴミを削除
    while min_h and cnt[min_h[0]] == 0:
        heapq.heappop(min_h)


def clean_max():
    # cntが0なのに、ピープの先頭に溜まったゴミを削除
    while max_h and cnt[-max_h[0]] == 0:
        heapq.heappop(max_h)


for _ in range(Q):
    t, *rest = map(int, input().split())
    if t == 1:
        x = rest[0]
        push(x)
    elif t == 2:
        x, c = rest
        discard(x, c)  # ここではヒープの中身は削除しない（t==3で削除）
    else:  # t == 3
        clean_min()  # ヒープのゴミを削除(クレンジング)
        clean_max()  # ヒープのゴミを削除(クレンジング)
        if not min_h:  # 空
            print(0)
        else:
            mn = min_h[0]
            mx = -max_h[0]
            print(mx - mn)

"""
ヒープ（クエリ処理）
チャッピー

ヒープから直接「特定値を c 個減らす」ことはできない！！※リストは可能
ので、削除クエリでは cnt[x] を減らすだけ
（ヒープは途中要素を削除するとヒープ構造が崩れてしまうので再構築が必要になってしまうため。
先頭要素のみ用意に削除できるので、t==3のときに初めて削除している!!頭いい!!）

ヒープの先頭を使うときに、cnt[top] == 0 なら「古いゴミ」なのでポップして捨てる
→ これをクレンジングと呼ぶ

https://atcoder.jp/contests/abc253/tasks/abc253_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68ddfacd-547c-8323-a3a2-e2b1f2e6f2e7
"""
