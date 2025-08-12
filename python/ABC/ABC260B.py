class Entry:
    def __init__(self, score, id):
        self.score = score
        self.id = id

    def sort_key(self):
        # 得点降順・同点はid昇順
        return (-self.score, self.id)


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

math = [Entry(A[i], i + 1) for i in range(N)]
eng = [Entry(B[i], i + 1) for i in range(N)]
both = [Entry(A[i] + B[i], i + 1) for i in range(N)]

math.sort(key=lambda e: e.sort_key())
eng.sort(key=lambda e: e.sort_key())
both.sort(key=lambda e: e.sort_key())

ans = []

cnt = 0
for e in math:
    if cnt == X:
        break
    if e.id not in ans:
        ans.append(e.id)
        cnt += 1

cnt = 0
for e in eng:
    if cnt == Y:
        break
    if e.id not in ans:
        ans.append(e.id)
        cnt += 1

cnt = 0
for e in both:
    if cnt == Z:
        break
    if e.id not in ans:
        ans.append(e.id)
        cnt += 1

ans.sort()
print(*ans, sep='\n')
