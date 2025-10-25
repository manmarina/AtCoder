from collections import Counter
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
# logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


N = int(input())
A = list(map(int, input().split()))

cnt1 = Counter(A)
logging.debug(f"{cnt1 = }")
cnt2 = [v for v in cnt1.values()]
logging.debug(f"{cnt2 = }")


def nC2(n):
    return n * (n - 1) // 2


total_count = len(A)
ans = 0
for c in cnt2:
    if c != 1:
        combi = nC2(c)
        count = total_count - c
        ans += combi * count

logging.debug(f"{combi = },{count = }")
print(ans)

"""
RE
"""
