class Student:
    def __init__(self, id, math, eng):
        self.id = id
        self.math = math
        self.eng = eng
        self.both = math + eng

    # def __repr__(self):
    # return f"(id={self.id}, math={self.math}, eng={self.eng},
    # both={self.both})"


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

students = [Student(i + 1, A[i], B[i]) for i in range(N)]

ans = []

cnt = 0
for s in sorted(students, key=lambda x: (-x.math, x.id)):
    if cnt == X:
        break
    if s.id not in ans:
        ans.append(s.id)
        cnt += 1

# print(sorted(students, key=lambda x: (-x.math, x.id)))
# print(ans)

cnt = 0
for s in sorted(students, key=lambda x: (-x.eng, x.id)):
    if cnt == Y:
        break
    if s.id not in ans:
        ans.append(s.id)
        cnt += 1

# print(sorted(students, key=lambda x: (-x.eng, x.id)))
# print(ans)

cnt = 0
for s in sorted(students, key=lambda x: (-x.both, x.id)):
    if cnt == Z:
        break
    if s.id not in ans:
        ans.append(s.id)
        cnt += 1

# print(sorted(students, key=lambda x: (-x.both, x.id)))
# print(ans)

ans.sort()
print(*ans, sep='\n')
