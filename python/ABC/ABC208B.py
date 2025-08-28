P = int(input())

# 1! 〜 10! を作る
facts = [1]
for x in range(2, 11):
    facts.append(facts[-1] * x)

ans = 0
for coin in reversed(facts):  # 10!, 9!, ..., 1!
    use = min(100, P // coin)  # 各額面は最大100枚まで
    ans += use
    P -= use * coin
print(ans)
