import math

A, B, H, M = map(int, input().split())

speed_A = 360 / (12 * 60)  # 短針の角度の分速
speed_B = 360 / 60  # 長針の角度の分速

hour = H * 60 + M  # 分に変換
minute = M

deg_A = hour * speed_A  # 短針の角度
deg_B = minute * speed_B  # 長針の角度

# print(deg_A)
# print(deg_B)

deg = max(deg_A, deg_B) - min(deg_A, deg_B)  # 2辺のなす角度を求める
# print(deg)

rad = math.radians(deg)  # ラジアンに変換
dist = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(rad))  # 余弦定理
print(dist)

"""
余弦定理

時計の短針長針の長さと、2辺のなす角度から、短針と長針の先端の間の距離を求める

https://atcoder.jp/contests/abc168/tasks/abc168_c
https://chatgpt.com/c/68f8d838-66ac-8320-8028-74ccc0b2a390
"""
