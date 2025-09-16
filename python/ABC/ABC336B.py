N = int(input())

count = 0
for i in range(len(bin(N))):
    if N >> i & 1 == 0:
        count += 1
    else:
        print(count)
        break
"""
ビット演算
1がでてくるまでビットを右にシフト（2で割り続ける）
1がでてくるまでのシフト回数が0の数と一致
"""
