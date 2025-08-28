s = input()       # 例: "9012"
xs = list(map(int, s))      # 文字→数値の配列 [9,0,1,2]

all_same = (len(set(s)) == 1)
is_step = all((xs[i] + 1) % 10 == xs[i + 1] for i in range(3))

print("Weak" if all_same or is_step else "Strong")
