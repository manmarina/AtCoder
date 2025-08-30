N = int(input().strip())
S = [input().strip() for _ in range(N)]

need = {'W': 'L', 'L': 'W', 'D': 'D'}

# 対称チェック（i<j だけでOK）
for i in range(N):
    for j in range(i + 1, N):
        a, b = S[i][j], S[j][i]
        if a not in need or need[a] != b:  # 今回は a not in needはなくて良い
            print("incorrect")
            exit()

print("correct")
