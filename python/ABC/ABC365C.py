N, M = map(int, input().split())
A = list(map(int, input().split()))

# 全額補助する資金がある時
if sum(A) <= M:
    print("infinite")
    exit()


def ok(n):
    temp = sum(min(n, A[i]) for i in range(N))  # 全員にn円までで支給するのを試す
    if temp <= M:
        return True  # 予算の範囲内の時
    else:
        return False  # 予算オーバーの時


# 二分探索 右寄せ版
l = 0  # 最小値
r = max(A)  # 最大値
while l < r:
    mid = (l + r + 1) // 2   # ← 右寄せ（+1 がポイント）
    if ok(mid):              # mid が OK ならもっと右へ
        l = mid
    else:                    # mid が NG なら左へ
        r = mid - 1

# l が「最大の OK」
print(l)

"""
解を二分探索
リトライ
解を二分探索のテンプレを活用。
上限額の最大値を求めたいので右寄せ版を使用。
解説+チャッピーと同じロジックで完成！

https://atcoder.jp/contests/abc365/tasks/abc365_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690f6b27-9b94-8322-ba41-9f450365912b
"""
