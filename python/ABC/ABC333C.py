base = [1]
for _ in range(15):  # 12桁で良いが、安全のため15桁
    base.append(base[-1] * 10 + 1)  # 最後の要素を10倍して1を足す
# print("base:", base)

all_nums = []
for x in base:
    for y in base:
        for z in base:
            all_nums.append(x + y + z)  # すべての組み合わせの和を格納
# print("all_nums", all_nums)

all_nums = sorted(set(all_nums))  # 重複を排除してソート

N = int(input())
print(all_nums[N - 1])  # 0-indexed

"""
全探索
12 桁以下のトリレプユニット数を列挙する
それらの 3 つの和で表される数を重複なしで列挙する
そのうちの N番目の数を求める

けんちょん
https://drken1215.hatenablog.com/entry/2024/11/02/190153

https://atcoder.jp/contests/abc333/tasks/abc333_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c454e-dc18-8321-8196-a41fb9edb5f7
"""
