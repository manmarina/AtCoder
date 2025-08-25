N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
alice = a[0::2]
bob = a[1::2]
print(sum(alice) - sum(bob))
