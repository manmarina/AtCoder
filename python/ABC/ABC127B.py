r, D, x = map(int, input().split())

algae = [x]
for i in range(1, 10 + 1):
    algae.append(r * algae[i - 1] - D)

print(*algae[1:], sep='\n')
