N = int(input())
L = list(map(int, input().split()))

longest = max(L)
other = sum(L) - longest
print("Yes" if other > longest else "No")
