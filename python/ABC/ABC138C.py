N = int(input())
V = list(map(int, input().split()))

V.sort()
ans = V[0]
for i in range(1, N):
    ans = (ans + V[i]) / 2
print(ans)

"""
基本実装問題

何も考えずに実装できたが、念の為解説を確認
公式は理解不能
こちらは偶然全く同じ解答の解説
https://compro.asukatagui.com/abc138c/
"""
