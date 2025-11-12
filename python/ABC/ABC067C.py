N = int(input())
A = list(map(int, input().split()))

cs = [0]  # Aの累積和を作成
for i in range(N):
    cs.append(cs[i] + A[i])
# print(cs)

ans = 3 * 10**9  # 制約より余裕のある数値
for i in range(1, N):
    ans = min(ans, abs(cs[-1] - cs[i] * 2))  # |x - y|を計算して最小値なら更新
print(ans)

"""
工夫して探索の通り数を減らす全探索 + 累積和
累積和を利用して、|x - y|の計算を高速化

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/01/01/220428

https://atcoder.jp/contests/abc067/tasks/arc078_a
"""
