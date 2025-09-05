N = int(input())
A = list(map(int, input().split()))

mx, imx = -1, -1  # max,maxのインデックス
smx, ismx = -1, -1  # 2番目のmax, 2番目のmaxのインデックス

for i, a in enumerate(A, start=1):  # 1-indexed位置を保持
    if a > mx:
        smx, ismx = mx, imx
        mx, imx = a, i
    elif a > smx:
        smx, ismx = a, i

print(ismx)
