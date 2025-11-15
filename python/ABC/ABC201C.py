S = input()

ans = 0

for num in range(10000):  # 0000〜9999
    code = f"{num:04d}"  # 4桁の文字列

    ok = True

    for d in range(10):
        if S[d] == 'o' and str(d) not in code:  # oなのにcodeに入っていない時はFalse
            ok = False
        if S[d] == 'x' and str(d) in code:  # xなのにcodeに入っていたらFalse
            ok = False

    if ok:
        ans += 1

print(ans)

"""
全探索
公式解説
制約が小さいので全探索可能。
候補の数字にoの数字が入っていない時、xの数字が入っているときは成立しない。

https://atcoder.jp/contests/abc201/tasks/abc201_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69185596-ff48-8322-8e2f-9ea4d7bf0a18
"""
