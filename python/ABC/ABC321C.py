K = int(input())

cnt = 0
num = 1
ans = []
while cnt < K:
    snum = str(num)
    for i in range(len(snum) - 1):
        if int(snum[i]) - int(snum[i + 1]) < 1:
            num += 1
            break
    else:
        cnt += 1
        ans.append(num)
        num += 1
print(ans[-1])

"""
TLE
"""
