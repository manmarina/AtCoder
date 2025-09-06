X = int(input().strip())

i = 2
while X > 1:
    assert X % i == 0  # 保証があるので実際は不要　階乗でない数値の時にエラーを発生
    X //= i
    i += 1
print(i - 1)
