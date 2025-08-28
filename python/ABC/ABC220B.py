
K = int(input())
A, B = input().split()


def to_dec(s: str, K: int) -> int:
    v = 0
    for ch in s:
        # d = ord(ch) - ord('0')  # 問題では桁は0~9のみ
        d = int(ch)
        v = v * K + d
    return v


a = to_dec(A, K)
b = to_dec(B, K)
print(a * b)
