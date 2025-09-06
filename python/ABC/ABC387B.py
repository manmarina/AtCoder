X = int(input())

# 表の中のXの数cntを求める　cntはXを割り切ることができる1〜9の整数
cnt = sum(1 for d in range(1, 10) if X % d == 0 and X // d <= 9)
print(2025 - X * cnt)
