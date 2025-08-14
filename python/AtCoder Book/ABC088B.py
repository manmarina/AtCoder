N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = [v for i, v in enumerate(a) if i % 2 == 0]
bob = [v for i, v in enumerate(a) if i % 2 == 1]

# print(a)
# print(alice)
# print(bob)
print(sum(alice) - sum(bob))
