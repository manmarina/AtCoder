N = int(input())

ans = set()  # リストだと、約数に平方根があると同じ数字が重複してWAになる
for i in range(1, int(N**0.5) + 1):  # 平方根まで探索
    if N % i == 0:
        ans.add(i)
        ans.add(N // i)
ans = sorted(ans)
print(*ans, sep='\n')


"""
約数列挙
完全に約数列挙！！！！！

https://atcoder.jp/contests/abc180/tasks/abc180_c
https://drken1215.hatenablog.com/entry/2020/10/21/194700
"""
