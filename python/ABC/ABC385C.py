N = int(input())
H = list(map(int, input().split()))

ans = 1
for i in range(N):
    for j in range(i + 1, N):
        if H[i] != H[j]:
            continue

        # Hi = Hjの時、さらに伸ばしてゆく
        cnt = 2
        k = j
        l = j + j - i
        while l < N and H[k] == H[l]:
            cnt += 1
            k = l
            l = l + j - i
        ans = max(ans, cnt)

print(ans)

"""
全探索
調べるべきものは O(N^2)通りある。
それぞれの場合に対して、等しい値がどこまで続くかを求めるのには O(N)の計算量を要するので、
全体として O(N3)の計算量となる。
実はちゃんと計算量解析すると、上記の全探索解法の計算量は O(N2logN)でもあることが言えて、これでも通る。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/12/25/021000

https://atcoder.jp/contests/abc385/tasks/abc385_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69135f68-9700-8321-972a-894de77cbdaf
"""
