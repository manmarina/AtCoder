N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 甘い料理を試す
A.sort(reverse=True)
# print(A)
ans = 10**9
for i in range(N):
    X -= A[i]  # 甘さを引く
    if X < 0:  # 甘さの許容値が0未満になったら
        ans = min(ans, i + 1)  # 食べた料理の最小値を更新

# しょっぱい料理を試す
B.sort(reverse=True)
# print(B)
for i in range(N):
    Y -= B[i]  # しょっぱさを引く
    if Y < 0:  # しょっぱさの許容値が0未満になったら
        ans = min(ans, i + 1)  # 食べた料理の最小値を更新

if ans == 10**9:  # 甘さも、しょっぱさも、許容値に達しなければ
    print(N)  # すべての料理の個数を出力
else:
    print(ans)  # 食べた料理の最小値を出力

"""
貪欲法
より甘い料理から食べるのとよりしょっぱい料理から食べるのを2通り試す。
2通りの最小値が答え。

https://atcoder.jp/contests/abc364/tasks/abc364_c
"""
