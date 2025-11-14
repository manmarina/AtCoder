A, B, X = map(int, input().split())


def ok(n):
    price = A * n + B * len(str(n))
    if price <= X:
        return True  # 予算内ならTrue
    else:
        return False  # 予算オーバーならFalse


l, r = 0, X  # 予算Xより大きい数字は買えないので、最大値はXに設定
while l < r:
    mid = (l + r + 1) // 2   # ← 右寄せ（+1 がポイント）
    if ok(mid):              # mid が OK ならもっと右へ
        l = mid
    else:                    # mid が NG なら左へ
        r = mid - 1
# l が「最大の OK」

if l >= 10**9:
    print(10 ** 9)  # お店には10^9までの数字しか売っていない
else:
    print(l)

"""
解を二分探索
解を二分探索のテンプレを活用。
買うことのできる最も大きい整数を求める問題なので、右寄せ版を使用する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/01/05/154700

https://atcoder.jp/contests/abc146/tasks/abc146_c
"""
