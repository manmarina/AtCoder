c = [list(map(int, input().split())) for _ in range(3)]

# print(c)

# c1の差を取得
d01 = c[0][0] - c[0][1]
d12 = c[0][1] - c[0][2]

# c2の差、c3の差とも、c1の差と同様か確認
for i in range(1, 3):
    if c[i][0] - c[i][1] != d01 or c[i][1] - c[i][2] != d12:
        print("No")
        break
else:
    print("Yes")
