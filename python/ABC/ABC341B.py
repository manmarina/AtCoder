N = int(input())
A = list(map(int, input().split()))
ST = [list(map(int, input().split())) for _ in range(N - 1)]
# print(A)
# print(ST)

for i in range(N - 1):
    A[i + 1] += A[i] // ST[i][0] * ST[i][1]
# print(A)
print(A[-1])

"""
一次元DPというより“貪欲な左→右の一回走査”
通貨は「国 i → i+1」にしか流れません。戻せないので、各 i でできる両替は全部やるのが最適です。
理由：目的は最終国 N の通貨最大化。途中の通貨を温存しても右へ送れなくなるだけで得しません。
"""
