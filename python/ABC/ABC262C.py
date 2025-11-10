N = int(input())
A = list(map(int, input().split()))
# print(A)

straight = 0  # min=ai,max=ajの場合
cross = 0  # min=aj,max=aiの場合
for i in range(N):
    if A[i] == i + 1:  # 0-indexed
        straight += 1
    else:
        if A[A[i] - 1] == i + 1:  # 0-indexed
            cross += 1

# print("straight:", straight)
# print("cross:", cross)

# straightのペアはnC2、crossのペアは1ペアを2回カウントしているので2で割る
print(straight * (straight - 1) // 2 + cross // 2)

"""
問題文の理解が難解系 + 数え上げ問題
リトライ

問題文の条件を読み解くのが難しい。
(Ai=i かつ Aj=j)または(Ai=jかつAj=i)
が導けるかが鍵となる。
1回目に比べて、問題文の理解は容易だった。

https://atcoder.jp/contests/abc262/tasks/abc262_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df27aa-e4b0-8321-93be-9d88bd81e47d
"""
