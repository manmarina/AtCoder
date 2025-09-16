from math import cos, sin, radians


a, b, d = map(int, input().split())

rad = radians(d)  # radianに変換
x = a * cos(rad) - b * sin(rad)  # xを原点を中心に反時計回りにrad回転
y = b * cos(rad) + a * sin(rad)  # yを原点を中心に反時計回りにrad回転

print(x, y)

"""
三角関数
回転の公式
任意点周りの回転移動を２通り解説！プログラムで自動化！
https://youta-blog.com/rotate_point
"""
