S = input()
nums = []
for s in S:
    nums.append(int(s))
# print(nums)

cnt = 0
N = len(nums)
for i in range(N - 1):
    # print(i)
    l = nums[i] + 1
    r = nums[i + 1]
    if l == r:
        cnt += 1
        j = 1

        while (i - j >= 0 and
               i + 1 + j <= N - 1 and
               nums[i - j] + 1 == nums[i + 1 + j]):
            cnt += 1
            j += 1

print(cnt)

"""
WA
"""
