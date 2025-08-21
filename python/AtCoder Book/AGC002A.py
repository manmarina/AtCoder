a, b = map(int, input().split())

if a <= 0 <= b:                  # 区間に 0 が含まれる
    print("Zero")
elif a > 0:                      # すべて正
    print("Positive")
else:                            # すべて負（b < 0）
    n = b - a + 1                # 要素数
    print("Negative" if n % 2 == 1 else "Positive")
