N = int(input())

ST = {}
for i in range(N):
    s, t = input().split()
    t = int(t)
    ST[s] = t

mountains = sorted(ST.items(), key=lambda x: x[1], reverse=True)
mountains = [list(mountain) for mountain in mountains]
print(mountains[1][0])
