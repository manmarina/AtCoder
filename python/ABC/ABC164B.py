A, B, C, D = map(int, input().split())

# t_T = ceil(C / B)
t_T = (C + B - 1) // B  # 高橋→青木
# t_A = ceil(A / D)
t_A = (A + D - 1) // D  # 青木→高橋

print("Yes" if t_T <= t_A else "No")
