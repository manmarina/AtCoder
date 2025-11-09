N, M = map(int, input().split())
A = list(map(int, input().split()))

# 全額補助する資金がある時
if sum(A) <= M:
    print("infinite")
    exit()

# midを判定


def ok(mid):
    total = sum(min(a, mid) for a in A)
    if total <= M:
        return True
    else:
        return False


# 　右寄せ版（最大値を求める）
left, right = 0, max(A)
while left < right:
    mid = (left + right + 1) // 2  # ← 右寄せ（+1 がポイント）
    if ok(mid):
        left = mid
    else:
        right = mid - 1

print(left)

"""
解を二分探索
解説+チャッピー
解を二分探索のテンプレを活用。
上限額の最大値を求めたいので右寄せ版を使用。

https://atcoder.jp/contests/abc365/tasks/abc365_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690f6b27-9b94-8322-ba41-9f450365912b
"""
