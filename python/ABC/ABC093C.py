v = list(map(int, input().split()))

odd = 0
even = 0
for i in range(3):
    if v[i] % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0

# 調整してすべての数の偶奇を揃える
# すべて偶数の場合、すべて奇数の場合は調整不要
if odd == 2:
    ans += 1
    for i in range(3):
        if v[i] % 2 == 1:  # 奇数を偶数にする
            v[i] += 1
elif even == 2:
    ans += 1
    for i in range(3):
        if v[i] % 2 == 0:  # 偶数を奇数にする（奇数と奇数の差は偶数なので）
            v[i] += 1

ma = max(v)
for i in range(3):
    ans += (ma - v[i]) // 2

print(ans)

"""
数学的気づき系
偶奇を考える。
奇数と奇数の差は偶数！！

hamayanhamayan
https://blog.hamayanhamayan.com/entry/2018/04/08/111125

https://atcoder.jp/contests/abc093/tasks/arc094_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690d583b-5cfc-8321-9677-0d186ebc8824
"""
